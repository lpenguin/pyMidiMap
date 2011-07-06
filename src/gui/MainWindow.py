'''
Created on 28.06.2011

@author: prian
'''
import PyQt4
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import *
from PyQt4.QtGui import QFileDialog, QStyle
from PyQt4.QtGui import QMessageBox

from forms.Ui_MainWindow import Ui_MainWindow
from MidiSettingsDialog import MidiSettingsDialog
from MidiMapDialog import MidiMapDialog
from classes.Settings import Settings
from classes.MidiMapper import *
import copy
import rtmidi
import sys
import pickle

from gui.LogDialog import LogDialog

class MainWindow(QMainWindow, Ui_MainWindow):    
    settings = Settings()
    fileName = None
    
    def initPorts(self):
        self.settings.midiInPort = 0
        self.settings.midiOutPort = 0
        self.openPorts()
        self.connect( self, SIGNAL('newLogMessage'), self.printToLog)

    def setSettings(self, _settings):
        self.settings = _settings
        self.midiSettingsDialog.settings = self.settings
        self.midiSettingsDialog.midiIn = self.midiIn
        self.midiSettingsDialog.midiOut = self.midiOut
        self.midiMapDialog.settings = self.settings
        self.logDialog.settings = self.settings
        self.initPorts()
        
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        style = PyQt4.QtGui.qApp.style()

        self.actionOpen.setIcon( QStyle.standardIcon( style ,QStyle.SP_DialogOpenButton ))
        self.actionSave.setIcon( QStyle.standardIcon( style ,QStyle.SP_DialogSaveButton ))
        self.actionNew.setIcon( QStyle.standardIcon( style ,QStyle.SP_FileIcon ))
        #self.actionOpen.setIcon( QStyle.standardIcon( style ,QStyle.SP_DialogOpenButton ))
                                        #self.mapList.setModel(self.midiMapModel)
        self.midiSettingsDialog = MidiSettingsDialog( self )
        self.midiMapDialog = MidiMapDialog( self )
        self.logDialog = LogDialog( self )
        self.midiIn = rtmidi.RtMidiIn()
        self.midiOut = rtmidi.RtMidiOut()
        self.midiMapper = MidiMapper(self.midiIn, self.midiOut)
        self.midiMapper.maps = self.mapList.maps()
        #self.connect(self.midiMapper, SIGNAL('midiCaptured( midi )'), self, SLOT( 'midiCaptured(self, midi )') )
        self.midiMapper.midiSignal.connect( self.midiCaptured )
        self.midiMapper.remapSignal.connect( self.midiRemapped )


    def tableCellDoubleClicked(self, row, column):
        self.editMap()

    def openPorts(self):
        try:
            self.midiIn.closePort()
            self.midiIn.cancelCallback()
            self.midiIn.openPort( self.settings.midiInPort )
            self.midiIn.setCallback( self.midiMapper.midiCallback )
            self.midiOut.closePort()
            self.midiOut.openPort( self.settings.midiOutPort )
        except rtmidi.Error, err:
            QMessageBox.critical(self, 'Open ports error', err.message)
            self.settings.midiInPort = 0
            self.settings.midiOutPort = 0

    def showMidiWindow(self):
        if self.midiSettingsDialog.exec_() == QDialog.Accepted:
            self.openPorts()
        
        
    def addMap(self):
        self.midiMapper.stopRemap()
        self.midiMapDialog.map = MidiMap()
        if self.midiMapDialog.exec_() == QDialog.Accepted:
            self.mapList.addMidiMap(self.midiMapDialog.map)
        self.midiMapper.startRemap()



    def editMap(self):
        self.midiMapper.stopRemap()
        row  = self.mapList.currentRow()
        if row == -1:
            return
        self.midiMapDialog.map = self.mapList.getMidiMap( row )
        if self.midiMapDialog.exec_() == QDialog.Accepted:
            self.mapList.setMidiMap( row, self.midiMapDialog.map)
        self.midiMapper.startRemap()

    
    def removeMap(self):
        row  = self.mapList.currentRow()
        if row == -1:
            return
        self.mapList.removeMidiMap( row )


    def duplicateMap(self):
        self.midiMapper.stopRemap()
        row  = self.mapList.currentRow()
        if row == -1:
            return
        map = copy.deepcopy( self.mapList.getMidiMap( row ) )
        self.midiMapDialog.map = map
        if self.midiMapDialog.exec_() == QDialog.Accepted:
            self.mapList.addMidiMap( self.midiMapDialog.map)
        self.midiMapper.startRemap()

    def showLog(self):
        self.logDialog.show()

    def openTriggered(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open Mappings', '', 'Maps (*.map)')
        if not fileName.endsWith('.map'):
            fileName+='.map'
        self.open( fileName )
        self.fileName = fileName

    def open(self, fileName):
        try:
            with open(fileName, 'r') as f:
                maps = pickle.load(f)
                self.mapList.setMaps(maps)
        except :
            print 'open error'

    def save(self, filename):
        try:
            maps = self.mapList.maps()
            with open(filename, 'w') as f:
                pickle.dump( maps , f, pickle.HIGHEST_PROTOCOL)
        except :
            print 'save error'

    
    def saveTriggered(self):
        if not self.fileName:
            self.saveAsTriggered()
        else:
            self.save(self.fileName)
        

    def saveAsTriggered(self):
        fileName = QFileDialog.getSaveFileName(self, 'Save Mappings', '', 'Maps (*.map)')
        if not fileName.endsWith('.map'):
            fileName+='.map'

        self.save( fileName )
        self.fileName = fileName


    def sendToLog(self, message):
        self.emit(SIGNAL('newLogMessage'), message)

    def printToLog(self, message):
        if self.logDialog.logEdit.toPlainText():
            self.logDialog.logEdit.setPlainText('%s\n%s' % (self.logDialog.logEdit.toPlainText(), message) )
        else:
            self.logDialog.logEdit.setPlainText( message )

    def midiCaptured(self, midi):
        self.sendToLog('captured: '+midiToStr(midi))
        if self.midiMapDialog.isVisible():
            data = midi2data( midi )
            self.midiMapDialog.midiCaptured( data )

    def midiRemapped(self, midi):
        self.sendToLog('remapped: '+midiToStr(midi))
