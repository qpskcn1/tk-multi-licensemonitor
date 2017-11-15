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
from subprocess import check_output

# by importing QT from sgtk rather than directly, we ensure that
# the code will be compatible with both PySide and PyQt.
from sgtk.platform.qt import QtCore, QtGui
from .ui.dialog import Ui_Dialog

# import the spinner_widget module from the qtwidgets framework
spinner_widget = sgtk.platform.import_framework(
    "tk-framework-qtwidgets", "spinner_widget")


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
        
        # most of the useful accessors are available through the Application class instance
        # it is often handy to keep a reference to this. You can get it via the following method:
        self._app = sgtk.platform.current_bundle()
        self.path = os.path.dirname(os.path.realpath(__file__))
        
        # via the self._app handle we can for example access:
        # - The engine, via self._app.engine
        # - A Shotgun API instance, via self._app.shotgun
        # - A tk API instance, via self._app.tk 

        # lastly, set up our very basic UI

        self.ui.textBrowser.setText("Choose Application to see license info")

        self.ui.NukeBtn.clicked.connect(self.checkNukeLicense)
        self.ui.ArnoldBtn.clicked.connect(self.checkArnoldLicense)
        self.ui.DeadlineBtn.clicked.connect(self.checkDeadlineLicense)

    def checkNukeLicense(self):
        # spinner = spinner_widget.SpinnerWidget(self)
        # spinner.setFixedSize(QtCore.QSize(100, 100))
        # spinner.show()
        rlmcmd = self.path + "\\rlmutil.exe rlmstat -c 4101@192.168.10.250 -i foundry -avail"
        rlmresult = check_output(rlmcmd)

        self.ui.textBrowser.setText("%s" % rlmresult)

    def checkArnoldLicense(self):
        try:
            flexlmcmd = self.path + "\\lmutil lmstat -a -c 27001@ofgsr-mpio1.local"
            flexresult = check_output(flexlmcmd)

            self.ui.textBrowser.setText("%s" % flexresult)
        except Exception as e:
            self.ui.textBrowser.setText("%s" % e)


    def checkDeadlineLicense(self):
        try:
            flexlmcmd = self.path + "\\lmutil lmstat -a -c 27008@ofgsr-mpio1.local"
            flexresult = check_output(flexlmcmd)

            self.ui.textBrowser.setText("%s" % flexresult)
        except Exception as e:
            self.ui.textBrowser.setText("%s" % e)
