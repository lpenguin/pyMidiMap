# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/prian/workspace/pyMidiMap/src/gui/forms/MidiMapDialog.ui'
#
# Created: Wed Jul  6 16:15:05 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MidiMapDialog(object):
    def setupUi(self, MidiMapDialog):
        MidiMapDialog.setObjectName(_fromUtf8("MidiMapDialog"))
        MidiMapDialog.resize(504, 276)
        self.verticalLayout = QtGui.QVBoxLayout(MidiMapDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mapperTabBox = QtGui.QTabWidget(MidiMapDialog)
        self.mapperTabBox.setObjectName(_fromUtf8("mapperTabBox"))
        self.MidiInputTab = QtGui.QWidget()
        self.MidiInputTab.setObjectName(_fromUtf8("MidiInputTab"))
        self.gridLayout = QtGui.QGridLayout(self.MidiInputTab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.MidiInputTab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.MidiInputTab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 7, 2, 1, 1)
        self.midiCaptureCheckBox = QtGui.QCheckBox(self.MidiInputTab)
        self.midiCaptureCheckBox.setChecked(True)
        self.midiCaptureCheckBox.setObjectName(_fromUtf8("midiCaptureCheckBox"))
        self.gridLayout.addWidget(self.midiCaptureCheckBox, 6, 2, 1, 1)
        self.inEventCombo = QtGui.QComboBox(self.MidiInputTab)
        self.inEventCombo.setObjectName(_fromUtf8("inEventCombo"))
        self.inEventCombo.addItem(_fromUtf8(""))
        self.inEventCombo.addItem(_fromUtf8(""))
        self.inEventCombo.addItem(_fromUtf8(""))
        self.inEventCombo.addItem(_fromUtf8(""))
        self.inEventCombo.addItem(_fromUtf8(""))
        self.inEventCombo.addItem(_fromUtf8(""))
        self.inEventCombo.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.inEventCombo, 2, 2, 1, 1)
        self.label = QtGui.QLabel(self.MidiInputTab)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.MidiInputTab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.inChannelCombo = QtGui.QComboBox(self.MidiInputTab)
        self.inChannelCombo.setObjectName(_fromUtf8("inChannelCombo"))
        self.inChannelCombo.addItem(_fromUtf8(""))
        self.inChannelCombo.addItem(_fromUtf8(""))
        self.inChannelCombo.addItem(_fromUtf8(""))
        self.inChannelCombo.addItem(_fromUtf8(""))
        self.inChannelCombo.addItem(_fromUtf8(""))
        self.inChannelCombo.addItem(_fromUtf8(""))
        self.inChannelCombo.addItem(_fromUtf8(""))
        self.inChannelCombo.addItem(_fromUtf8(""))
        self.inChannelCombo.addItem(_fromUtf8(""))
        self.inChannelCombo.addItem(_fromUtf8(""))
        self.inChannelCombo.addItem(_fromUtf8(""))
        self.inChannelCombo.addItem(_fromUtf8(""))
        self.inChannelCombo.addItem(_fromUtf8(""))
        self.inChannelCombo.addItem(_fromUtf8(""))
        self.inChannelCombo.addItem(_fromUtf8(""))
        self.inChannelCombo.addItem(_fromUtf8(""))
        self.inChannelCombo.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.inChannelCombo, 0, 2, 1, 1)
        self.inValue1Edit = QtGui.QLineEdit(self.MidiInputTab)
        self.inValue1Edit.setObjectName(_fromUtf8("inValue1Edit"))
        self.gridLayout.addWidget(self.inValue1Edit, 4, 2, 1, 1)
        self.inValue2Edit = QtGui.QLineEdit(self.MidiInputTab)
        self.inValue2Edit.setObjectName(_fromUtf8("inValue2Edit"))
        self.gridLayout.addWidget(self.inValue2Edit, 5, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.MidiInputTab)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 4, 3, 1, 1)
        self.label_10 = QtGui.QLabel(self.MidiInputTab)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 5, 3, 1, 1)
        self.mapperTabBox.addTab(self.MidiInputTab, _fromUtf8(""))
        self.ActionTab = QtGui.QWidget()
        self.ActionTab.setObjectName(_fromUtf8("ActionTab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.ActionTab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.outMidiRadioButton = QtGui.QRadioButton(self.ActionTab)
        self.outMidiRadioButton.setChecked(True)
        self.outMidiRadioButton.setObjectName(_fromUtf8("outMidiRadioButton"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.outMidiRadioButton)
        self.frame = QtGui.QFrame(self.ActionTab)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.outChannelCombo = QtGui.QComboBox(self.frame)
        self.outChannelCombo.setObjectName(_fromUtf8("outChannelCombo"))
        self.outChannelCombo.addItem(_fromUtf8(""))
        self.outChannelCombo.addItem(_fromUtf8(""))
        self.outChannelCombo.addItem(_fromUtf8(""))
        self.outChannelCombo.addItem(_fromUtf8(""))
        self.outChannelCombo.addItem(_fromUtf8(""))
        self.outChannelCombo.addItem(_fromUtf8(""))
        self.outChannelCombo.addItem(_fromUtf8(""))
        self.outChannelCombo.addItem(_fromUtf8(""))
        self.outChannelCombo.addItem(_fromUtf8(""))
        self.outChannelCombo.addItem(_fromUtf8(""))
        self.outChannelCombo.addItem(_fromUtf8(""))
        self.outChannelCombo.addItem(_fromUtf8(""))
        self.outChannelCombo.addItem(_fromUtf8(""))
        self.outChannelCombo.addItem(_fromUtf8(""))
        self.outChannelCombo.addItem(_fromUtf8(""))
        self.outChannelCombo.addItem(_fromUtf8(""))
        self.outChannelCombo.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.outChannelCombo, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.outEventCombo = QtGui.QComboBox(self.frame)
        self.outEventCombo.setObjectName(_fromUtf8("outEventCombo"))
        self.outEventCombo.addItem(_fromUtf8(""))
        self.outEventCombo.addItem(_fromUtf8(""))
        self.outEventCombo.addItem(_fromUtf8(""))
        self.outEventCombo.addItem(_fromUtf8(""))
        self.outEventCombo.addItem(_fromUtf8(""))
        self.outEventCombo.addItem(_fromUtf8(""))
        self.outEventCombo.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.outEventCombo, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.outValue1Edit = QtGui.QLineEdit(self.frame)
        self.outValue1Edit.setEnabled(True)
        self.outValue1Edit.setText(_fromUtf8(""))
        self.outValue1Edit.setObjectName(_fromUtf8("outValue1Edit"))
        self.gridLayout_2.addWidget(self.outValue1Edit, 2, 1, 1, 1)
        self.outValue1Combo = QtGui.QComboBox(self.frame)
        self.outValue1Combo.setObjectName(_fromUtf8("outValue1Combo"))
        self.outValue1Combo.addItem(_fromUtf8(""))
        self.outValue1Combo.addItem(_fromUtf8(""))
        self.outValue1Combo.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.outValue1Combo, 2, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.outValue2Edit = QtGui.QLineEdit(self.frame)
        self.outValue2Edit.setEnabled(True)
        self.outValue2Edit.setText(_fromUtf8(""))
        self.outValue2Edit.setObjectName(_fromUtf8("outValue2Edit"))
        self.gridLayout_2.addWidget(self.outValue2Edit, 4, 1, 1, 1)
        self.outValue2Combo = QtGui.QComboBox(self.frame)
        self.outValue2Combo.setObjectName(_fromUtf8("outValue2Combo"))
        self.outValue2Combo.addItem(_fromUtf8(""))
        self.outValue2Combo.addItem(_fromUtf8(""))
        self.outValue2Combo.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.outValue2Combo, 4, 2, 1, 1)
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.frame)
        self.ouKeyRadioButton = QtGui.QRadioButton(self.ActionTab)
        self.ouKeyRadioButton.setObjectName(_fromUtf8("ouKeyRadioButton"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.ouKeyRadioButton)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.outKeysLabel = KeysEdit(self.ActionTab)
        self.outKeysLabel.setEnabled(False)
        self.outKeysLabel.setReadOnly(True)
        self.outKeysLabel.setObjectName(_fromUtf8("outKeysLabel"))
        self.horizontalLayout.addWidget(self.outKeysLabel)
        self.clearButton = QtGui.QPushButton(self.ActionTab)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout.addWidget(self.clearButton)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.mapperTabBox.addTab(self.ActionTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.mapperTabBox)
        self.buttonBox = QtGui.QDialogButtonBox(MidiMapDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(MidiMapDialog)
        self.mapperTabBox.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MidiMapDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MidiMapDialog.reject)
        QtCore.QObject.connect(self.ouKeyRadioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MidiMapDialog.keySequenceClicked)
        QtCore.QObject.connect(self.outMidiRadioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MidiMapDialog.midiMessageClicked)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("pressed()")), MidiMapDialog.clearButtonPressed)
        QtCore.QMetaObject.connectSlotsByName(MidiMapDialog)

    def retranslateUi(self, MidiMapDialog):
        MidiMapDialog.setWindowTitle(QtGui.QApplication.translate("MidiMapDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MidiMapDialog", "Value 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MidiMapDialog", "Value 2", None, QtGui.QApplication.UnicodeUTF8))
        self.midiCaptureCheckBox.setText(QtGui.QApplication.translate("MidiMapDialog", "Midi Capture", None, QtGui.QApplication.UnicodeUTF8))
        self.inEventCombo.setItemText(0, QtGui.QApplication.translate("MidiMapDialog", "Any", None, QtGui.QApplication.UnicodeUTF8))
        self.inEventCombo.setItemText(1, QtGui.QApplication.translate("MidiMapDialog", "Note On", None, QtGui.QApplication.UnicodeUTF8))
        self.inEventCombo.setItemText(2, QtGui.QApplication.translate("MidiMapDialog", "Note Off", None, QtGui.QApplication.UnicodeUTF8))
        self.inEventCombo.setItemText(3, QtGui.QApplication.translate("MidiMapDialog", "Aftertouch", None, QtGui.QApplication.UnicodeUTF8))
        self.inEventCombo.setItemText(4, QtGui.QApplication.translate("MidiMapDialog", "Control", None, QtGui.QApplication.UnicodeUTF8))
        self.inEventCombo.setItemText(5, QtGui.QApplication.translate("MidiMapDialog", "Program Change", None, QtGui.QApplication.UnicodeUTF8))
        self.inEventCombo.setItemText(6, QtGui.QApplication.translate("MidiMapDialog", "Pitchbend", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MidiMapDialog", "Event", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MidiMapDialog", "Channel", None, QtGui.QApplication.UnicodeUTF8))
        self.inChannelCombo.setItemText(0, QtGui.QApplication.translate("MidiMapDialog", "Any", None, QtGui.QApplication.UnicodeUTF8))
        self.inChannelCombo.setItemText(1, QtGui.QApplication.translate("MidiMapDialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.inChannelCombo.setItemText(2, QtGui.QApplication.translate("MidiMapDialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.inChannelCombo.setItemText(3, QtGui.QApplication.translate("MidiMapDialog", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.inChannelCombo.setItemText(4, QtGui.QApplication.translate("MidiMapDialog", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.inChannelCombo.setItemText(5, QtGui.QApplication.translate("MidiMapDialog", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.inChannelCombo.setItemText(6, QtGui.QApplication.translate("MidiMapDialog", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.inChannelCombo.setItemText(7, QtGui.QApplication.translate("MidiMapDialog", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.inChannelCombo.setItemText(8, QtGui.QApplication.translate("MidiMapDialog", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.inChannelCombo.setItemText(9, QtGui.QApplication.translate("MidiMapDialog", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.inChannelCombo.setItemText(10, QtGui.QApplication.translate("MidiMapDialog", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.inChannelCombo.setItemText(11, QtGui.QApplication.translate("MidiMapDialog", "11", None, QtGui.QApplication.UnicodeUTF8))
        self.inChannelCombo.setItemText(12, QtGui.QApplication.translate("MidiMapDialog", "12", None, QtGui.QApplication.UnicodeUTF8))
        self.inChannelCombo.setItemText(13, QtGui.QApplication.translate("MidiMapDialog", "13", None, QtGui.QApplication.UnicodeUTF8))
        self.inChannelCombo.setItemText(14, QtGui.QApplication.translate("MidiMapDialog", "14", None, QtGui.QApplication.UnicodeUTF8))
        self.inChannelCombo.setItemText(15, QtGui.QApplication.translate("MidiMapDialog", "15", None, QtGui.QApplication.UnicodeUTF8))
        self.inChannelCombo.setItemText(16, QtGui.QApplication.translate("MidiMapDialog", "16", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MidiMapDialog", "* Empty means any value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MidiMapDialog", "* Empty means any value", None, QtGui.QApplication.UnicodeUTF8))
        self.mapperTabBox.setTabText(self.mapperTabBox.indexOf(self.MidiInputTab), QtGui.QApplication.translate("MidiMapDialog", "Midi Input", None, QtGui.QApplication.UnicodeUTF8))
        self.outMidiRadioButton.setText(QtGui.QApplication.translate("MidiMapDialog", "Midi Message", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MidiMapDialog", "Channel", None, QtGui.QApplication.UnicodeUTF8))
        self.outChannelCombo.setItemText(0, QtGui.QApplication.translate("MidiMapDialog", "Same as input", None, QtGui.QApplication.UnicodeUTF8))
        self.outChannelCombo.setItemText(1, QtGui.QApplication.translate("MidiMapDialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.outChannelCombo.setItemText(2, QtGui.QApplication.translate("MidiMapDialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.outChannelCombo.setItemText(3, QtGui.QApplication.translate("MidiMapDialog", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.outChannelCombo.setItemText(4, QtGui.QApplication.translate("MidiMapDialog", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.outChannelCombo.setItemText(5, QtGui.QApplication.translate("MidiMapDialog", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.outChannelCombo.setItemText(6, QtGui.QApplication.translate("MidiMapDialog", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.outChannelCombo.setItemText(7, QtGui.QApplication.translate("MidiMapDialog", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.outChannelCombo.setItemText(8, QtGui.QApplication.translate("MidiMapDialog", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.outChannelCombo.setItemText(9, QtGui.QApplication.translate("MidiMapDialog", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.outChannelCombo.setItemText(10, QtGui.QApplication.translate("MidiMapDialog", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.outChannelCombo.setItemText(11, QtGui.QApplication.translate("MidiMapDialog", "11", None, QtGui.QApplication.UnicodeUTF8))
        self.outChannelCombo.setItemText(12, QtGui.QApplication.translate("MidiMapDialog", "12", None, QtGui.QApplication.UnicodeUTF8))
        self.outChannelCombo.setItemText(13, QtGui.QApplication.translate("MidiMapDialog", "13", None, QtGui.QApplication.UnicodeUTF8))
        self.outChannelCombo.setItemText(14, QtGui.QApplication.translate("MidiMapDialog", "14", None, QtGui.QApplication.UnicodeUTF8))
        self.outChannelCombo.setItemText(15, QtGui.QApplication.translate("MidiMapDialog", "15", None, QtGui.QApplication.UnicodeUTF8))
        self.outChannelCombo.setItemText(16, QtGui.QApplication.translate("MidiMapDialog", "16", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MidiMapDialog", "Event", None, QtGui.QApplication.UnicodeUTF8))
        self.outEventCombo.setItemText(0, QtGui.QApplication.translate("MidiMapDialog", "Same as input", None, QtGui.QApplication.UnicodeUTF8))
        self.outEventCombo.setItemText(1, QtGui.QApplication.translate("MidiMapDialog", "Note On", None, QtGui.QApplication.UnicodeUTF8))
        self.outEventCombo.setItemText(2, QtGui.QApplication.translate("MidiMapDialog", "Note Off", None, QtGui.QApplication.UnicodeUTF8))
        self.outEventCombo.setItemText(3, QtGui.QApplication.translate("MidiMapDialog", "Aftertouch", None, QtGui.QApplication.UnicodeUTF8))
        self.outEventCombo.setItemText(4, QtGui.QApplication.translate("MidiMapDialog", "Control", None, QtGui.QApplication.UnicodeUTF8))
        self.outEventCombo.setItemText(5, QtGui.QApplication.translate("MidiMapDialog", "Program Change", None, QtGui.QApplication.UnicodeUTF8))
        self.outEventCombo.setItemText(6, QtGui.QApplication.translate("MidiMapDialog", "Pitchbend", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MidiMapDialog", "Value 1", None, QtGui.QApplication.UnicodeUTF8))
        self.outValue1Combo.setItemText(0, QtGui.QApplication.translate("MidiMapDialog", "Same as input", None, QtGui.QApplication.UnicodeUTF8))
        self.outValue1Combo.setItemText(1, QtGui.QApplication.translate("MidiMapDialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.outValue1Combo.setItemText(2, QtGui.QApplication.translate("MidiMapDialog", "Assign", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MidiMapDialog", "Value 2", None, QtGui.QApplication.UnicodeUTF8))
        self.outValue2Combo.setItemText(0, QtGui.QApplication.translate("MidiMapDialog", "Same as input", None, QtGui.QApplication.UnicodeUTF8))
        self.outValue2Combo.setItemText(1, QtGui.QApplication.translate("MidiMapDialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.outValue2Combo.setItemText(2, QtGui.QApplication.translate("MidiMapDialog", "Assign", None, QtGui.QApplication.UnicodeUTF8))
        self.ouKeyRadioButton.setText(QtGui.QApplication.translate("MidiMapDialog", "Key Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("MidiMapDialog", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.mapperTabBox.setTabText(self.mapperTabBox.indexOf(self.ActionTab), QtGui.QApplication.translate("MidiMapDialog", "Action", None, QtGui.QApplication.UnicodeUTF8))

from gui.KeysEdit import KeysEdit
