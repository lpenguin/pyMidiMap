'''
Created on 28.06.2011

@author: prian
'''
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import *

from forms.Ui_MainWindow import Ui_MainWindow
from MidiSettingsDialog import MidiSettingsDialog
from MidiMapDialog import MidiMapDialog
from classes.Settings import Settings
from classes.MidiMap import *
from MidiMapModel import *
import copy
import rtmidi
import classes.pykey

from gui.LogDialog import LogDialog

class MainWindow(QMainWindow, Ui_MainWindow):    
    settings = Settings()

    def midiCallback(self, midiMessage):
        self.print_message( midiMessage )

    def messageToStr(self, midi):
        str = 'msg'
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
        elif midi.isPitchWeel():
            str = ''.join( ['PITCHWEEL: ', midi.getPitchWheelValue()] )
        return  str

    def print_message(self, midi):
        str = self.messageToStr(midi)
        self.mapMidiMessage( midi )
        self.sendToLog(str)

    def sendToLog(self, message):
        self.emit(SIGNAL('newLogMessage'), message)
        
    def printToLog(self, message):
        if self.logDialog.logEdit.toPlainText():
            self.logDialog.logEdit.setPlainText('%s\n%s' % (self.logDialog.logEdit.toPlainText(), message) )
        else:
            self.logDialog.logEdit.setPlainText( message )

    
    def mapMidiMessage(self, midiMessage):
        for map in self.mapList.maps():
            self.processMidiMessage( map, midiMessage)

    def processMidiMessage(self, map, midi):
        if self.processFilter( map, midi ):
            print "Filter ok"
            self.processAction(map, midi)

    def processAction(self, map, midi):
        print "remapping midi"

        data = self.translateRawData(midi)
        resMidi = rtmidi.MidiMessage()
        channel = midi.getChannel()
        action = map.action
        if isinstance(map.action, MidiMessageAction):
            print "message"

            value1 = data.value1
            value2 = data.value2
            if action.value1.type != Modify.Same:
                value1 = action.value1.value

            if action.value2.type != Modify.Same:
                value2 = action.value2.value

            if action.channel:
                channel = action.channel
            if action.event == EventType.Any:
                midi.setChannel(channel)
                resMidi = midi
            elif action.event == EventType.NoteOn:
                resMidi = rtmidi.MidiMessage.noteOn(channel, value1, value2 )
            elif action.event == EventType.NoteOff:
                resMidi = rtmidi.MidiMessage.noteOff(channel, value1 )
            elif action.event == EventType.Aftertouch:
                resMidi = rtmidi.MidiMessage.aftertouchChange( chennel, value1, value2)
            elif action.event == EventType.Control:
                resMidi = rtmidi.MidiMessage.controllerEvent( channel, value1, value2)
            elif action.event == EventType.ProgramChange:
                resMidi = rtmidi.MidiMessage.programChange( channel, value1)
            elif action.event == EventType.Pitchbend:
                resMidi = rtmidi.MidiMessage.pitchWheel( channel, value1)
            else:
                self.sendToLog('wrong message')
                return
        else:
            print "keys"+" ".join(action.keys)
            classes.pykey.send_string("".join(action.keys))
        print self.messageToStr(midi)
        self.settings.midiOut.sendMessage( resMidi )


    def translateRawData(self, midi):
        channel = midi.getChannel()
        
        value1 = None
        value2 = None
        if midi.isNoteOn():
            value1 = midi.getNoteNumber()
            value2 = midi.getVelocity()
        elif midi.isNoteOff():
            value1 = midi.getNoteNumber()
        elif  midi.isProgramChange():
            value1 = midi.getProgramChangeNumber()
    
        return { "channel": channel, "value1": value1, "value2": value2 }

    def getEvent(self, midi ):
        if midi.isNoteOn():
            return EventType.NoteOn
        if midi.isNoteOff():
            return EventType.NoteOff
        if midi.isAftertouch():
            return EventType.Aftertouch
        if midi.isController():
            return EventType.Control
        if midi.isProgramChange():
            return EventType.ProgramChange
        if midi.isPitchWeel():
            return EventType.Pitchbend
        return None
    
    def processFilter(self, map, midi):
        if map.message.channel != 0 and map.message.channel != midi.getChannel():
            return False
        if map.message.event != EventType.Any and map.message.event != self.getEvent( midi ):
            return False

        data = midi.getRawData()
        dt1 = None
        dt2 = None
        if len( data ) >= 2:
            dt1 = ord( data[1] )
        if len( data ) >= 3:
            dt2 = ord( data[2] )

        if map.message.value1 != '' and dt1 != None and map.message.data1 != dt1:
            return False
        if map.message.value2 != '' and dt2 != None and map.message.data1 != dt2:
            return False

        return True
    
    def initPorts(self):
        self.settings.midiIn.openPort(0)
        self.settings.midiOut.openPort(0)
        self.settings.midiIn.setCallback( self.midiCallback )
        self.settings.midiInPort = 0
        self.settings.midiOutPort = 0
        self.connect( self, SIGNAL('newLogMessage'), self.printToLog)
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
