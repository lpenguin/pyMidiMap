__author__ = 'prian'

from classes.MidiMap import *
import rtmidi
import sys
from classes.KeySender import *
from PyQt4.QtCore import QObject
import traceback

class MidiMapper(QObject):
    
    def __init__(self, parent = None):
        QObject.__init__(self, parent)
        self.midiIn = None
        self.midiOut = None
        self.maps = []
        
    def processAction(self, map, midi):
        print "remapping midi"
        action = map.action
        try:
            if isinstance(map.action, MidiMessageAction):
                print "message"
                data = midi2data(midi)
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

        if map.message.value1 != '' and dt1 and map.message.data1 != dt1:
            return False
        if map.message.value2 != '' and dt2 and map.message.data1 != dt2:
            return False

        return True

    def remapMidiMessage(self, map, midi):
        if self.processFilter( map, midi ):
            print "Filter ok"
            self.processAction(map, midi)

    def processMidiMessage(self, midi):
        for map in self.maps:
            self.remapMidiMessage( map, midi)

    def midiCallback(self, midi):
        try:
            self.processMidiMessage( midi )
        except Exception, err:
            print "Exception:", err
            traceback.print_exc(file=sys.stdout)