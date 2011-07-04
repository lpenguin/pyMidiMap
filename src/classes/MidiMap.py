__author__ = 'prian'
from Misc import *

Modify = enum('Same', 'Add', 'Assign')
EventType = enum('Any', 'NoteOn', 'NoteOff', 'Aftertouch', 'Control', 'ProgramChange', 'Pitchbend')

class MidiMessage(object):
    channel = 0
    event = EventType.Any
    value1 = ''
    value2 = ''
    def __init__(self, channel = 0, event = EventType.Any, value1 = '', value2 = ''):
        self.channel = channel
        self.event = event
        self.value1 = value1
        self.value2 = value2

    def toString(self):
        return 'channel: '+str(self.channel)+', event: '+enumKey(EventType, self.event)+\
               ', value1: '+self.value1+', value2: '+self.value2

class MappedValue(object):
    type = 0
    value = 0
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
    keys = []
    def __init__(self, keys = []):
        self.keys = keys

    def toString(self):
        return 'keys: '+', '.join(self.keys)

class MidiMessageAction(MapAction):
    channel = 0
    event = EventType.Any
    value1 = MappedValue('')
    value2 = MappedValue('')

    def __init__(self, channel = 0, event = EventType.Any, value1 = MappedValue(''), value2 = MappedValue('')):
        self.channel = channel
        self.event = event
        self.value1 = value1
        self.value2 = value2
    def toString(self):
        modifyers = []
        if self.channel != 0:
            modifyers.append('channel = %s'%(self.channel))
        if self.event != 0:
            modifyers.append('event =  %s'%( enumKey(EventType, self.event)))
        if self.value1.type != Modify.Same:
            modifyers.append('value1 %s'%( self.value1.toString() ))
        if self.value2.type != Modify.Same:
            modifyers.append('value2 %s'%( self.value2.toString() ))

        return 'midi: %s' % (', '.join(modifyers))

class MidiMap(object):
    message = MidiMessage()
    action  = MidiMessageAction()

    def __init__(self, message = MidiMessage(), action = MidiMessageAction()):
        self.message = message
        self.action = action

    def actionString(self):
        return self.action.toString()

    def messageString(self):
        return self.message.toString()