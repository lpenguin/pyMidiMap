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

    def midiCallback(self, midiMessage):
        self.print_message( midiMessage )

    def print_message(self, midi):
        str = ''
        if midi.isNoteOn():
            str = '%s %s %s'%( 'ON: ', midi.getMidiNoteName(midi.getNoteNumber()) , midi.getVelocity() )
        elif midi.isNoteOff():
            str = ''.join( ['OFF:', midi.getMidiNoteName(midi.getNoteNumber())] )
        elif midi.isController():
            str = ''.join( ['CONTROLLER', midi.getControllerNumber(), midi.getControllerValue()] )
        elif midi.isSysEx():
            str = ''.join( ['SYSEX (%i bytes)' % midi.getSysExData()] )
        elif midi.isAftertouch():
            str = ''.join( ['AFTERTOUCH: ', midi.getAfterTouchValue()] )
        print( str )
        self.mapMidiMessage( midi )
        #self.logDialog.logEdit.setPlainText('%s\n%s' % (self.logDialog.logEdit.toPlainText(), str) )
        #self.logDialog.logEdit.toPlainText()+'\n'+

    def mapMidiMessage(self, midiMessage):
        for map in self.mapList.maps():
            self.processMidiMessage( map, midiMessage)

    def processMidiMessage(self, map, midi):
        if self.processFilter( map, midi ):
            self.processAction(map, midi)
            
    def processAction(self, map, midi):
        pass
    
    def processFilter(self, map, midi):
        if map.message.channel != '' and map.message.status != midi.getChannel():
            return False
        if map.message.status != '' and map.message.status != midi.getStatus():
            return False

        data = midi.getRawData()
        dt1 = None
        dt2 = None
        if len( data ) >= 2:
            dt1 = ord( data[1] )
        if len( data ) >= 3:
            dt2 = ord( data[2] )

        if map.message.data1 != '' and dt1 != None and map.message.data1 != dt1:
            return False
        if map.message.data2 != '' and dt2 != None and map.message.data1 != dt2:
            return False

        return True
    
    def initPorts(self):
        self.settings.midiIn.openPort(0)
        self.settings.midiOut.openPort(0)
        self.settings.midiIn.setCallback( self.midiCallback )
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
