'''
Created on 28.06.2011

@author: prian
'''
from forms.Ui_midiForm import Ui_MidiForm
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QListWidgetItem
from classes.Settings import Settings

class MidiSettingsDialog(QDialog, Ui_MidiForm):
    
    settings = Settings()
    
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.midiIn = None
        self.midiOut = None
        #self.showMidiPorts()
    
    def showMidiPorts(self):
        self.midiInList.clear()
        self.midiOutList.clear()
        
        midiIn = self.midiIn
        ports = range(midiIn.getPortCount())
        for i in ports:
            self.midiInList.addItem(QListWidgetItem(midiIn.getPortName(i)))

        midiOut = self.midiOut
        ports = range(midiOut.getPortCount())
        for i in ports:
            self.midiOutList.addItem(QListWidgetItem(midiOut.getPortName(i)))

        
        if self.settings.midiInPort != None:
            self.midiInList.item(self.settings.midiInPort).setSelected(True)
            
        if self.settings.midiOutPort != None:
            self.midiOutList.item(self.settings.midiOutPort).setSelected(True)
    
    def exec_(self):
        self.showMidiPorts()
        return QDialog.exec_(self)
          
    def accept(self):
        inRow = self.midiInList.selectedIndexes().pop().row()
        outRow = self.midiOutList.selectedIndexes().pop().row()

        if inRow == -1:
            inRow = 0
        if outRow == -1:
            outRow = 0


        self.settings.midiInPort = inRow
        self.settings.midiOutPort = outRow
        QDialog.accept(self)
    
    def reject(self):
        QDialog.reject(self)