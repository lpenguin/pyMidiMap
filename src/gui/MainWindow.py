'''
Created on 28.06.2011

@author: prian
'''
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import *
from PyQt4.QtCore import QCoreApplication
from PyQt4.QtGui import QFileDialog

from forms.Ui_MainWindow import Ui_MainWindow
from MidiSettingsDialog import MidiSettingsDialog
from MidiMapDialog import MidiMapDialog
from classes.Settings import Settings
from classes.MidiMap import *
from classes.KeySender import SendKeyPress

import copy
import rtmidi
import sys
import pickle

from gui.LogDialog import LogDialog
import traceback

class MainWindow(QMainWindow, Ui_MainWindow):    
    settings = Settings()
    fileName = None
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

    def data2Midi(self, channel = 0, event = EventType.Any, value1 = None, value2 = None):
        
        if event == EventType.NoteOn:
            return rtmidi.MidiMessage.noteOn(channel, value1, value2 )
        elif event == EventType.NoteOff:
            return rtmidi.MidiMessage.noteOff(channel, value1 )
        elif event == EventType.Aftertouch:
            return rtmidi.MidiMessage.aftertouchChange( channel, value1, value2)
        elif event == EventType.Control:
            return rtmidi.MidiMessage.controllerEvent( channel, value1, value2)
        elif event == EventType.ProgramChange:
            return rtmidi.MidiMessage.programChange( channel, value1)
        elif event == EventType.Pitchbend:
            return rtmidi.MidiMessage.pitchWheel( channel, value1)
        
        return None

    def midi2data(self, midi):
        channel = midi.getChannel()
        value1 = None
        value2 = None
        event = None
        if midi.isNoteOn():
            event = EventType.NoteOn
            value1 = midi.getNoteNumber()
            value2 = midi.getVelocity()
        if midi.isNoteOff():
            event = EventType.NoteOff
            value1 = midi.getNoteNumber()
        if midi.isAftertouch():
            event = EventType.Aftertouch
            value1 = midi.getNoteNumber()
            value2 = midi.getAfterTouchValue()
        if midi.isController():
            event = EventType.Control
            value1 = midi.getControllerNumber()
            value2 = midi.getControllerValue()
        if midi.isProgramChange():
            event = EventType.ProgramChange
            value1 = midi.getProgramChangeNumber()
        if midi.isPitchWheel():
            event = EventType.Pitchbend
            value1 = midi.getPitchWheelValue()
        return dict( channel=channel, event = event, value1 = value1, value2 = value2 )

    def processAction(self, map, midi):
        print "remapping midi"
        action = map.action
        try:
            if isinstance(map.action, MidiMessageAction):
                print "message"
                data = self.midi2data(midi)
                value1 = data['value1']
                value2 = data['value2']
                event = data['event']
                channel = data['channel']

                if action.value1.type != Modify.Same:
                    value1 = action.value1.value
                if action.value2.type != Modify.Same:
                    value2 = action.value2.value
                if action.channel:
                    channel = action.channel
                if action.event != EventType.Any:
                    event = action.event

                resMidi = self.data2Midi( channel, event, value1, value2 )
                if resMidi:
                    self.settings.midiOut.sendMessage( resMidi )
                else:
                    print "wrong message"
            else:
                for key in action.keyCodes:
                    SendKeyPress(key)

        except Exception, err:
            print "Exception:", err
            traceback.print_exc(file=sys.stdout)
            
        except :
            print "Unexpected error:", sys.exc_info()[0]
            traceback.print_exc(file=sys.stdout)
            #classes.pykey.send_string("".join(action.keys))




#    def translateRawData(self, midi):
#        channel = midi.getChannel()
#        
#        value1 = None
#        value2 = None
#        if midi.isNoteOn():
#            value1 = midi.getNoteNumber()
#            value2 = midi.getVelocity()
#        elif midi.isNoteOff():
#            value1 = midi.getNoteNumber()
#        elif  midi.isProgramChange():
#            value1 = midi.getProgramChangeNumber()
#
#        return { "channel": channel, "value1": value1, "value2": value2 }


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

    def openTriggered(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open Mappings', '', 'Maps (*.map)')
        if not fileName.endsWith('.map'):
            fileName+='.map'
        self.open( fileName )
        self.fileName = fileName

    def open(self, fileName):
        #try:
        maps = None
        with open(fileName, 'r') as f:
            maps = pickle.load(f)
            self.mapList.setMaps(maps)
        bas = maps
        #except :
        #    print 'file error'

    def save(self, filename):
        #try:
        maps = self.mapList.maps()
        with open(filename, 'w') as f:
            pickle.dump( maps , f, pickle.HIGHEST_PROTOCOL)
        #except :
        #    print 'file error'

    
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