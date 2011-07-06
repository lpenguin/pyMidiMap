__author__ = 'prian'
from Misc import *

Modify = enum('Same', 'Add', 'Assign')
EventType = enum('Any', 'NoteOn', 'NoteOff', 'Aftertouch', 'Control', 'ProgramChange', 'Pitchbend')

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

def messageToStr(self, midi):
    text = 'msg'
    if midi.isNoteOn():
        text = '%s %s %s'%( 'ON: ', midi.getMidiNoteName(midi.getNoteNumber()) , midi.getVelocity() )
    elif midi.isNoteOff():
        text = ''.join( ['OFF:', midi.getMidiNoteName(midi.getNoteNumber())] )
    elif midi.isController():
        text = ''.join( ['CONTROLLER', str(midi.getControllerNumber()), str(midi.getControllerValue())] )
    elif midi.isSysEx():
        text = ''.join( ['SYSEX (%i bytes)' % midi.getSysExData()] )
    elif midi.isAftertouch():
        text = ''.join( ['AFTERTOUCH: ', midi.getAfterTouchValue()] )
    elif midi.isPitchWheel():
        text = ''.join( ['PITCHWHEEL: ', str(midi.getPitchWheelValue())] )
    elif midi.isProgramChange():
        text = ''.join( ['PROGRAM: ', str(midi.getProgramChangeNumber())] )
    #else:
    #    print 'Unknown midi'
    return  text

class MidiMessage(object):
    def __init__(self, channel = 0, event = EventType.Any, value1 = '', value2 = ''):
        self.channel = channel
        self.event = event
        self.value1 = value1
        self.value2 = value2

    def toString(self):
        channel = str( self.channel or 'Any' )
        event = enumKey(EventType, self.event)
        value1 = self.value1 or 'Any'
        value2 = self.value2 or 'Any'

        return 'channel: %s, event: %s, value1: %s, value2: %s' % (channel, event, value1, value2)

class MappedValue(object):
    def __init__(self, value=0, type = Modify.Same):
        self.type = type
        self.value = value
        
    def toString(self):
        if self.type == Modify.Add:
            return "+= "+self.value
        elif self.type == Modify.Same:
            return 'same'
        else:
            return "= "+self.value
        
    def modify(self, value):
        if self.type == Modify.Same:
            return value
        elif self.type == Modify.Add:
            return self.value + value
        else:
            return self.value
        
class MapAction(object):
    def __init__(self):
        pass
    def toString(self):
        return ''
    
class KeyPressAction(MapAction):
    def __init__(self, keys = None, keyCodes = None):
        self.keys = keys or []
        self.keyCodes = keyCodes
        MapAction.__init__(self)
    def toString(self):
        return 'keys: '+', '.join(self.keys)

class MidiMessageAction(MapAction):
    def __init__(self, channel = 0, event = EventType.Any, value1 = MappedValue(''), value2 = MappedValue('')):
        self.channel = channel
        self.event = event
        self.value1 = value1
        self.value2 = value2
        MapAction.__init__(self)
    def toString(self):
        modifiers = []
        if self.channel:
            modifiers.append( 'channel = %s'% self.channel  )
        if self.event:
            modifiers.append('event =  %s'%( enumKey(EventType, self.event)))
        if self.value1.type != Modify.Same:
            modifiers.append('value1 %s'%( self.value1.toString() ))
        if self.value2.type != Modify.Same:
            modifiers.append('value2 %s'%( self.value2.toString() ))

        return 'midi: %s' % (', '.join(modifiers))

class MidiMap(object):
    def __init__(self, message = MidiMessage(), action = MidiMessageAction()):
        self.message = message
        self.action = action

    def actionString(self):
        return self.action.toString()

    def messageString(self):
        return self.message.toString()