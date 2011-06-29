__author__ = 'prian'
from Misc import *

Modify = enum('Add', 'Assign')

class MidiMessage(object):
    channel = 0
    status = 0
    data1 = 0
    data2 = 0
    def __init__(self, channel = '0', status = '0', data1 = '0', data2 = '0'):
        self.channel = channel
        self.status = status
        self.data1 = data1
        self.data2 = data2

    def toString(self):
        return 'ch '+self.channel+' st '+self.status+' d1 '+self.data1+' d2 '+self.data2

class MappedValue(object):
    type = 0
    value = 0
    def __init__(self, value=0, type = Modify.Add):
        self.type = type
        self.value = value
        
    def toString(self):
        if self.type == Modify.Add:
            return "+="+self.value
        else:
            return "="+self.value

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
    channel = MappedValue()
    status = MappedValue()
    data1 = MappedValue()
    data2 = MappedValue()

    def __init__(self, channel = MappedValue(), status = MappedValue(), data1 = MappedValue(), data2 = MappedValue()):
        self.channel = channel
        self.status = status
        self.data1 = data1
        self.data2 = data2
    def toString(self):
        return 'midi: ch%s st%s d1%s d2%s' % (self.channel.toString(), self.status.toString(), self.data1.toString(), self.data2.toString())


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