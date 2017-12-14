# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

import sgtk
import os
import traceback

# by importing QT from sgtk rather than directly, we ensure that
# the code will be compatible with both PySide and PyQt.
from sgtk.platform.qt import QtCore, QtGui
from .ui.dialog import Ui_Dialog
from .rlmreader import RLMReader
from .flexlmreader import FLEXLMReader

logger = sgtk.platform.get_logger(__name__)
task_manager = sgtk.platform.import_framework("tk-framework-shotgunutils", "task_manager")
shotgun_globals = sgtk.platform.import_framework("tk-framework-shotgunutils", "shotgun_globals")


class AppDialog(QtGui.QWidget):
    """
    Main application dialog window
    """

    def __init__(self):
        """
        Constructor
        """
        # first, call the base class and let it do its thing.
        QtGui.QWidget.__init__(self)

        # now load in the UI that was created in the UI designer
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # setup treeview
        self.treeview = self.ui.treeView
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['User', 'Time'])
        self.treeview.setModel(self.model)
        self.treeview.setUniformRowHeights(True)
        # most of the useful accessors are available through the Application class instance
        # it is often handy to keep a reference to this. You can get it via the following method:
        self._app = sgtk.platform.current_bundle()
        self.path = os.path.dirname(os.path.realpath(__file__))

        # create a background task manager
        self._task_manager = task_manager.BackgroundTaskManager(
            self,
            start_processing=True,
            max_threads=2
        )

        # lastly, set up our very basic UI
        license_server_info = self._app.get_setting("license_server_info")
        logger.debug(license_server_info)
        self.ui.textBrowser.setText("Choose Application to see license info")
        try:
            for info in license_server_info:
                self.createButton(info)
        except Exception as e:
            tb = traceback.format_exc()
            self.ui.textBrowser.setText("%s \n %s" % (e, tb))

    def createButton(self, info):
        button = QtGui.QPushButton(info["Application"])
        self.ui.ApplicationBtnLayout.addWidget(button)
        button.clicked.connect(self.checkLicense(info["LicenseManager"],
                                                 info["Port"],
                                                 info["Server"],
                                                 info["ISV"]))

    def checkLicense(self, lm, port, server, isv=None):
        def _checkLicense():
            self.ui.textBrowser.append("Fetching data...\n...\n...")
            QtGui.QApplication.processEvents()
            try:
                if lm == "RLM":
                    reader = RLMReader(self.path, port, server, isv)
                elif lm == "FLEXLM":
                    reader = FLEXLMReader(self.path, port, server)
                else:
                    raise Exception("Cannot Read License Manager %s" % lm)
                result = reader.getInfo()
                self.displayInTreeView(result)
                self.ui.textBrowser.append("Success!")
            except Exception as e:
                tb = traceback.format_exc()
                self.ui.textBrowser.setText("%s \n %s" % (e, tb))
        return _checkLicense

    def displayInTreeView(self, data):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(['User', 'Time'])
        font = QtGui.QFont()
        font.setPointSize(12)
        for licenseName in data:
            userInfo = data[licenseName]
            if not userInfo:
                continue
            parent = QtGui.QStandardItem("%s (%d/%d)"
                                         % (licenseName, userInfo[0][0], userInfo[0][1]))
            parent.setFont(font)
            for user in userInfo[1:]:
                child1 = QtGui.QStandardItem(user[0])
                child2 = QtGui.QStandardItem(user[1])
                parent.appendRow([child1, child2])
            self.model.appendRow(parent)
            # span container columns
            # self.treeview.setFirstColumnSpanned(i, self.treeview.rootIndex(), True)
        self.treeview.resizeColumnToContents(0)

    def closeEvent(self, event):
        """
        Executed when the main dialog is closed.
        All worker threads and other things which need a proper shutdown
        need to be called here.
        """
        logger.debug("CloseEvent Received. Begin shutting down UI.")

        # register the data fetcher with the global schema manager
        shotgun_globals.unregister_bg_task_manager(self._task_manager)

        try:
            # shut down main threadpool
            self._task_manager.shut_down()
        except Exception as e:
            logger.exception("Error running Shotgun Panel App closeEvent() %s" % e)
