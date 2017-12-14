# -*- coding: utf-8 -*-



# Form implementation generated from reading ui file 'dialog.ui'

#

# Created: Thu Dec 14 14:07:32 2017

#      by: pyside-uic 0.2.15 running on PySide 1.2.4

#

# WARNING! All changes made in this file will be lost!



from tank.platform.qt import QtCore, QtGui



class Ui_Dialog(object):

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")

        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)

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

        self.ApplicationBtnLayout = QtGui.QVBoxLayout()

        self.ApplicationBtnLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)

        self.ApplicationBtnLayout.setObjectName("ApplicationBtnLayout")

        self.gridLayout.addLayout(self.ApplicationBtnLayout, 0, 0, 2, 1)



        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def retranslateUi(self, Dialog):

        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

        self.HelpBtn.setText(QtGui.QApplication.translate("Dialog", "Help", None, QtGui.QApplication.UnicodeUTF8))



from . import resources_rc

