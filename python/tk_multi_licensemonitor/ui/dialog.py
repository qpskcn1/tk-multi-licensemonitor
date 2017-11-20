# -*- coding: utf-8 -*-



# Form implementation generated from reading ui file 'dialog.ui'

#

# Created: Mon Nov 20 14:17:38 2017

#      by: pyside-uic 0.2.15 running on PySide 1.2.4

#

# WARNING! All changes made in this file will be lost!



from tank.platform.qt import QtCore, QtGui



class Ui_Dialog(object):

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")

        Dialog.resize(806, 453)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)

        sizePolicy.setHorizontalStretch(0)

        sizePolicy.setVerticalStretch(0)

        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())

        Dialog.setSizePolicy(sizePolicy)

        self.gridLayout = QtGui.QGridLayout(Dialog)

        self.gridLayout.setObjectName("gridLayout")

        self.textBrowser = QtGui.QTextBrowser(Dialog)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)

        sizePolicy.setHorizontalStretch(0)

        sizePolicy.setVerticalStretch(0)

        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())

        self.textBrowser.setSizePolicy(sizePolicy)

        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 50))

        self.textBrowser.setObjectName("textBrowser")

        self.gridLayout.addWidget(self.textBrowser, 4, 2, 1, 1)

        self.HelpBtn = QtGui.QPushButton(Dialog)

        self.HelpBtn.setObjectName("HelpBtn")

        self.gridLayout.addWidget(self.HelpBtn, 4, 0, 1, 1)

        self.line = QtGui.QFrame(Dialog)

        self.line.setFrameShape(QtGui.QFrame.HLine)

        self.line.setFrameShadow(QtGui.QFrame.Sunken)

        self.line.setObjectName("line")

        self.gridLayout.addWidget(self.line, 3, 2, 1, 1)

        self.treeView = QtGui.QTreeView(Dialog)

        self.treeView.setObjectName("treeView")

        self.gridLayout.addWidget(self.treeView, 0, 2, 2, 1)

        self.verticalLayout = QtGui.QVBoxLayout()

        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)

        self.verticalLayout.setObjectName("verticalLayout")

        self.NukeBtn = QtGui.QPushButton(Dialog)

        self.NukeBtn.setObjectName("NukeBtn")

        self.verticalLayout.addWidget(self.NukeBtn)

        self.DeadlineBtn = QtGui.QPushButton(Dialog)

        self.DeadlineBtn.setObjectName("DeadlineBtn")

        self.verticalLayout.addWidget(self.DeadlineBtn)

        self.ArnoldBtn = QtGui.QPushButton(Dialog)

        self.ArnoldBtn.setObjectName("ArnoldBtn")

        self.verticalLayout.addWidget(self.ArnoldBtn)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 1)



        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def retranslateUi(self, Dialog):

        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

        self.HelpBtn.setText(QtGui.QApplication.translate("Dialog", "Help", None, QtGui.QApplication.UnicodeUTF8))

        self.NukeBtn.setText(QtGui.QApplication.translate("Dialog", "Nuke", None, QtGui.QApplication.UnicodeUTF8))

        self.DeadlineBtn.setText(QtGui.QApplication.translate("Dialog", "Deadline", None, QtGui.QApplication.UnicodeUTF8))

        self.ArnoldBtn.setText(QtGui.QApplication.translate("Dialog", "Arnold", None, QtGui.QApplication.UnicodeUTF8))



from . import resources_rc

