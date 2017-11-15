# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created: Tue Nov 14 18:55:09 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(714, 398)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.NukeBtn = QtGui.QPushButton(Dialog)
        self.NukeBtn.setObjectName("NukeBtn")
        self.verticalLayout.addWidget(self.NukeBtn)
        self.ArnoldBtn = QtGui.QPushButton(Dialog)
        self.ArnoldBtn.setObjectName("ArnoldBtn")
        self.verticalLayout.addWidget(self.ArnoldBtn)
        self.DeadlineBtn = QtGui.QPushButton(Dialog)
        self.DeadlineBtn.setObjectName("DeadlineBtn")
        self.verticalLayout.addWidget(self.DeadlineBtn)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.NukeBtn.setText(QtGui.QApplication.translate("Dialog", "Nuke", None, QtGui.QApplication.UnicodeUTF8))
        self.ArnoldBtn.setText(QtGui.QApplication.translate("Dialog", "Arnold", None, QtGui.QApplication.UnicodeUTF8))
        self.DeadlineBtn.setText(QtGui.QApplication.translate("Dialog", "Deadline", None, QtGui.QApplication.UnicodeUTF8))

