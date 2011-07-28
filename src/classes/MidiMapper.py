__author__ = 'prian'

from classes.MidiMap import *
import rtmidi
import sys
from classes.KeySender import *
from PyQt4.QtCore import QObject
from PyQt4.QtCore import *
import traceback

class MidiMapper(QObject):
    midiSignal = pyqtSignal( rtmidi.MidiMessage )
    remapSignal = pyqtSignal( rtmidi.MidiMessage )
    
    def __init__(self, midiIn = None, midiOut = None, parent = None):
        QObject.__init__(self, parent)
        self.midiIn = midiIn
        self.midiOut = midiOut
        self.maps = []
        self.__remapping = True

    def startRemap(self):
        self.__remapping = True

    def stopRemap(self):
        self.__remapping = False
        
    def processAction(self, map, midi):
        print "remapping midi"
        action = map.action
        try:
            if isinstance(map.action, MidiMessageAction):
                data = midi2data(midi)
                value1 = data['value1']
                value2 = data['value2']
                event = data['event']
                channel = data['channel']

                if action.value1.type != Modify.Same:
                    value1 = action.value1.modify( value1 )
                if action.value2.type != Modify.Same:
                    value2 = action.value2.modify( value2 )
                if action.channel:
                    channel = action.channel
                if action.event != EventType.Any:
                    event = action.event
                resMidi = data2Midi( channel, event, value1, value2 )
                if resMidi:
                    self.midiOut.sendMessage( resMidi )
                    self.remapSignal.emit( resMidi )
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

    def processFilter(self, map, midi):
        data = midi2data( midi )
        if map.message.channel != 0 and map.message.channel != data['channel']:
            return False
        if map.message.event != EventType.Any and map.message.event != data['event']:
            return False

        if map.message.value1 != '' and data['value1'] and int(map.message.value1) != data['value1']:#
            return False
        if map.message.value2 != '' and data['value2'] and int(map.message.value2) != data['value2']:
            return False
        return True

    def remapMidiMessage(self, map, midi):
        if self.processFilter( map, midi ):
            self.processAction(map, midi)

    def processMidiMessage(self, midi):
        for map in self.maps:
            self.remapMidiMessage( map, midi)

    def midiCallback(self, midi):
        try:
            #self.emit( QtCore.SIGNAL('midiCaptured'), midi)
            if self.__remapping:
                self.processMidiMessage( midi )
            self.midiSignal.emit( midi )
        except Exception, err:
            print "Exception:", err
            traceback.print_exc(file=sys.stdout)
        except :
            print "Unexpected error:", sys.exc_info()[0]
            traceback.print_exc(file=sys.stdout)