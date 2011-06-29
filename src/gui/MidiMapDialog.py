'''
Created on 28.06.2011

@author: prian
'''
from PyQt4.Qt import QString

from forms.Ui_MidiMapDialog import Ui_MidiMapDialog

from PyQt4.QtGui import QDialog

from classes.Settings import Settings
from classes.MidiMap import *

class MidiMapDialog(QDialog, Ui_MidiMapDialog):
    settings = Settings()
    map = MidiMap()
    
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
    def midiCaptureClicked(self):
        pass
    
    def keySequenceClicked(self):
        ch = self.ouKeyRadioButton.isChecked()
        
        self.outKeyEdit.setEnabled(ch)
        self.outChannelEdit.setEnabled(not ch )
        self.outStatusEdit.setEnabled(not ch )
        self.outData1Edit.setEnabled(not ch )
        self.outData2Edit.setEnabled(not ch )

        self.outChannelCombo.setEnabled(not ch)
        self.outStatusCombo.setEnabled(not ch)
        self.outData1Combo.setEnabled(not ch)
        self.outData2Combo.setEnabled(not ch)
    
    def midiMessageClicked(self):
        ch = self.outMidiRadioButton.isChecked()
        
        self.outKeyEdit.setEnabled(not ch)
        self.outChannelEdit.setEnabled( ch )
        self.outStatusEdit.setEnabled( ch )
        self.outData1Edit.setEnabled( ch )
        self.outData2Edit.setEnabled( ch )

        self.outChannelCombo.setEnabled( ch )
        self.outStatusCombo.setEnabled( ch )
        self.outData1Combo.setEnabled( ch )
        self.outData2Combo.setEnabled( ch )

    def combo2Modify(self, combo):
        if combo.currentIndex() == 0:
            return Modify.Add
        else:
            return Modify.Assign

    def modify2combo(self, combo, modify):
        if modify == Modify.Add:
            combo.setCurrentIndex( 0 )
        else:
            combo.setCurrentIndex( 1 )
        
    def exec_(self):
        self.inStatusEdit.setText(self.map.message.status)
        self.inChannelEdit.setText(self.map.message.channel)
        self.inData1Edit.setText(self.map.message.data1)
        self.inData2Edit.setText(self.map.message.data2)

        if isinstance(self.map.action, MidiMessageAction):
            self.ouKeyRadioButton.setChecked(False)
            self.outMidiRadioButton.setChecked(True)

            self.outKeyEdit.setText('')
            self.outChannelEdit.setText( QString(str(self.map.action.channel.value) ))
            self.outStatusEdit.setText( QString(str(self.map.action.status.value)) )
            self.outData1Edit.setText( QString(str(self.map.action.data1.value)) )
            self.outData2Edit.setText( QString(str(self.map.action.data2.value)) )

            self.modify2combo(self.outChannelCombo, self.map.action.channel.type )
            self.modify2combo(self.outStatusCombo, self.map.action.status.type )
            self.modify2combo(self.outData1Combo, self.map.action.data1.type )
            self.modify2combo(self.outData2Combo, self.map.action.data2.type )
        else:
            self.outChannelEdit.setText( '')
            self.outStatusEdit.setText( '' )
            self.outData1Edit.setText( '' )
            self.outData2Edit.setText( '' )
            keys = ''
            if self.map.action.keys:
                keys = ' '.join(self.map.action.keys)
            self.outKeyEdit.setText(keys)

        return QDialog.exec_(self)

    def accept(self):
        self.map.message.status = self.inStatusEdit.text()
        self.map.message.channel = self.inChannelEdit.text()
        self.map.message.data1 = self.inData1Edit.text()
        self.map.message.data2 = self.inData2Edit.text()

        if self.ouKeyRadioButton.isChecked():
            self.map.action = KeyPressAction(str(self.outKeyEdit.text()).split(' '))
        else:
            self.map.action = MidiMessageAction( MappedValue(str(self.outChannelEdit.text()), self.combo2Modify(self.outChannelCombo)),\
                                                 MappedValue(str(self.outStatusEdit.text()), self.combo2Modify(self.outStatusCombo)), \
                                                 MappedValue(str(self.outData1Edit.text()), self.combo2Modify(self.outData1Combo)), \
                                                 MappedValue(str(self.outData2Edit.text()), self.combo2Modify(self.outData2Combo)))
        QDialog.accept(self)