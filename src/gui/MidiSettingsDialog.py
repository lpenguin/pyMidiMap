'''
Created on 28.06.2011

@author: prian
'''
from forms.Ui_midiForm import Ui_MidiForm
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QListWidgetItem
from PyQt4.QtGui import QMessageBox

from classes.Settings import Settings

import rtmidi

class MidiSettingsDialog(QDialog, Ui_MidiForm):
    
    settings = Settings()
    
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.showMidiPorts()
    
    def showMidiPorts(self):
        self.midiInList.clear()
        self.midiOutList.clear()
        
        midiIn = self.settings.midiIn
        ports = range(midiIn.getPortCount())
        for i in ports:
            self.midiInList.addItem(QListWidgetItem(midiIn.getPortName(i)))


                    
        midiOut = self.settings.midiOut
        ports = range(midiOut.getPortCount())
        for i in ports:
            self.midiOutList.addItem(QListWidgetItem(midiOut.getPortName(i)))

        
        if self.settings.midiInPort != None:
            self.midiInList.item(self.settings.midiInPort).setSelected(True)
            
        if self.settings.midiOutPort != None:
            self.midiOutList.item(self.settings.midiOutPort).setSelected(True)
    
    def show(self):
        self.showMidiPorts()
        QDialog.show(self)
          
    def accept(self):
        self.settings.midiInPort = self.midiInList.currentRow()
        self.settings.midiOutPort = self.midiOutList.currentRow()
        QDialog.accept(self)
    
    def reject(self):
        QDialog.reject(self)