# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/prian/workspace/pyMidiMap/src/gui/forms/midiForm.ui'
#
# Created: Wed Jun 29 12:18:47 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MidiForm(object):
    def setupUi(self, MidiForm):
        MidiForm.setObjectName(_fromUtf8("MidiForm"))
        MidiForm.resize(560, 384)
        self.verticalLayout = QtGui.QVBoxLayout(MidiForm)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(MidiForm)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.midiInList = QtGui.QListWidget(MidiForm)
        self.midiInList.setObjectName(_fromUtf8("midiInList"))
        self.verticalLayout.addWidget(self.midiInList)
        self.label_2 = QtGui.QLabel(MidiForm)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.midiOutList = QtGui.QListWidget(MidiForm)
        self.midiOutList.setObjectName(_fromUtf8("midiOutList"))
        self.verticalLayout.addWidget(self.midiOutList)
        self.buttonBox = QtGui.QDialogButtonBox(MidiForm)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(MidiForm)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MidiForm.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MidiForm.reject)
        QtCore.QMetaObject.connectSlotsByName(MidiForm)

    def retranslateUi(self, MidiForm):
        MidiForm.setWindowTitle(QtGui.QApplication.translate("MidiForm", "Midi Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MidiForm", "Midi In Ports", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MidiForm", "Midi Out Ports", None, QtGui.QApplication.UnicodeUTF8))

