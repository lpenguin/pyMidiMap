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
        ch = not ch
        self.outChannelCombo.setEnabled( ch )
        self.outEventCombo.setEnabled( ch )
        self.outValue1Edit.setEnabled( ch )
        self.outValue2Edit.setEnabled( ch )
        self.outValue1Combo.setEnabled( ch )
        self.outValue2Combo.setEnabled( ch )

    
    def midiMessageClicked(self):
        ch = self.outMidiRadioButton.isChecked()
        self.outChannelCombo.setEnabled( ch )
        self.outEventCombo.setEnabled( ch )
        self.outValue1Edit.setEnabled( ch )
        self.outValue2Edit.setEnabled( ch )
        self.outValue1Combo.setEnabled( ch )
        self.outValue2Combo.setEnabled( ch )
        ch = not ch
        self.outKeyEdit.setEnabled(ch)
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
        self.inEventCombo.setCurrentIndex(self.map.message.event)
        self.inChannelCombo.setCurrentIndex(self.map.message.channel)
        self.inValue1Edit.setText( self.map.message.value1)
        self.inValue2Edit.setText( self.map.message.value2)
        
        #return QDialog.exec_(self)
        
        if isinstance(self.map.action, MidiMessageAction):
            self.ouKeyRadioButton.setChecked(False)
            self.outMidiRadioButton.setChecked(True)

            self.outKeyEdit.setText('')

            self.outChannelCombo.setCurrentIndex( self.map.action.channel )
            self.outEventCombo.setCurrentIndex( self.map.action.event )

            self.outValue1Edit.setText( QString(str(self.map.action.value1.value)) )
            self.outValue2Edit.setText( QString(str(self.map.action.value2.value)) )

            self.outValue1Combo.setCurrentIndex(self.map.action.value1.type)
            self.outValue2Combo.setCurrentIndex(self.map.action.value2.type)
            #self.modify2combo(self.outValue1Combo, self.map.action.value1.type )
            #self.modify2combo(self.outValue2Combo, self.map.action.value2.type )
        else:
            self.outChannelCombo.setCurrentIndex( 0 )
            self.outEventCombo.setCurrentIndex( 0 )
            self.outValue1Edit.setText( '' )
            self.outValue2Edit.setText( '' )
            #self.outChannelEdit.setText( '')
            #self.outStatusEdit.setText( '' )
            #self.outData1Edit.setText( '' )
            #self.outData2Edit.setText( '' )
            keys = ''
            if self.map.action.keys:
                keys = ' '.join(self.map.action.keys)
            self.outKeyEdit.setText(keys)

        return QDialog.exec_(self)

    def accept(self):
        self.map.message.event = self.inEventCombo.currentIndex()
        self.map.message.channel = self.inChannelCombo.currentIndex()
        self.map.message.value1 = self.inValue1Edit.text()
        self.map.message.value2 = self.inValue2Edit.text()

        if self.ouKeyRadioButton.isChecked():
            self.map.action = KeyPressAction(str(self.outKeyEdit.text()).split(' '))
        else:
            channel = self.outChannelCombo.currentIndex()
            event = self.outEventCombo.currentIndex()
            value1 = MappedValue( str( self.outValue1Edit.text() ), self.outValue1Combo.currentIndex() )
            value2 = MappedValue( str( self.outValue2Edit.text() ), self.outValue2Combo.currentIndex() )

            self.map.action = MidiMessageAction( channel, event, value1, value2 )
        QDialog.accept(self)