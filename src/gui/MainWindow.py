'''
Created on 28.06.2011

@author: prian
'''
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QDialog

from forms.Ui_MainWindow import Ui_MainWindow
from MidiSettingsDialog import MidiSettingsDialog
from MidiMapDialog import MidiMapDialog
from classes.Settings import Settings
from classes.MidiMap import *
from MidiMapModel import *
import copy

from gui.LogDialog import LogDialog

class MainWindow(QMainWindow, Ui_MainWindow):    
    settings = Settings()

    def initPorts(self):
        self.settings.midiIn.openPort(0)
        self.settings.midiOut.openPort(0)
        self.settings.midiInPort = 0
        self.settings.midiOutPort = 0
        
        pass
    def setSettings(self, _settings):
        self.settings = _settings
        self.midiSettingsDialog.settings = self.settings
        self.midiMapDialog.settings = self.settings
        self.logDialog.settings = self.settings
        self.initPorts()
        
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        #self.mapList.setModel(self.midiMapModel)
        self.midiSettingsDialog = MidiSettingsDialog( self )
        self.midiMapDialog = MidiMapDialog( self )
        self.logDialog = LogDialog( self )
        
    def showMidiWindow(self):
        self.midiSettingsDialog.show()
        
        
    def addMap(self):
        self.midiMapDialog.map = MidiMap
        if self.midiMapDialog.exec_() == QDialog.Accepted:
            self.mapList.addMidiMap(self.midiMapDialog.map)
    
    def editMap(self):
        row  = self.mapList.currentRow()
        if row == -1:
            return
        self.midiMapDialog.map = self.mapList.getMidiMap( row )
        if self.midiMapDialog.exec_() == QDialog.Accepted:
            self.mapList.setMidiMap( row, self.midiMapDialog.map)

    
    def removeMap(self):
        row  = self.mapList.currentRow()
        if row == -1:
            return
        self.mapList.removeMidiMap( row )


    def duplicateMap(self):
        row  = self.mapList.currentRow()
        if row == -1:
            return
        map = copy.deepcopy( self.mapList.getMidiMap( row ) )
        self.midiMapDialog.map = map
        if self.midiMapDialog.exec_() == QDialog.Accepted:
            self.mapList.addMidiMap( self.midiMapDialog.map)

    def showLog(self):
        self.logDialog.show()
