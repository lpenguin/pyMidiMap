# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/prian/workspace/pyMidiMap/src/gui/forms/LogDialog.ui'
#
# Created: Wed Jul  6 14:43:19 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_LogDialog(object):
    def setupUi(self, LogDialog):
        LogDialog.setObjectName(_fromUtf8("LogDialog"))
        LogDialog.resize(601, 606)
        self.verticalLayout = QtGui.QVBoxLayout(LogDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.logEdit = QtGui.QPlainTextEdit(LogDialog)
        self.logEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.logEdit.setReadOnly(True)
        self.logEdit.setBackgroundVisible(False)
        self.logEdit.setCenterOnScroll(True)
        self.logEdit.setObjectName(_fromUtf8("logEdit"))
        self.verticalLayout.addWidget(self.logEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.clearButton = QtGui.QPushButton(LogDialog)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout.addWidget(self.clearButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.closeButton = QtGui.QPushButton(LogDialog)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(LogDialog)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("pressed()")), LogDialog.close)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("pressed()")), self.logEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(LogDialog)

    def retranslateUi(self, LogDialog):
        LogDialog.setWindowTitle(QtGui.QApplication.translate("LogDialog", "Log", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("LogDialog", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("LogDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

