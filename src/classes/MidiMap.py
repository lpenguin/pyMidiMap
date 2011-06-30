__author__ = 'prian'
from Misc import *

Modify = enum('Add', 'Assign')

class MidiMessage(object):
    channel = ''
    status = ''
    data1 = ''
    data2 = ''
    def __init__(self, channel = '', status = '', data1 = '', data2 = ''):
        self.channel = channel
        self.status = status
        self.data1 = data1
        self.data2 = data2

    def toString(self):
        return 'ch: '+self.channel+', st: '+self.status+', d1: '+self.data1+', d2: '+self.data2

class MappedValue(object):
    type = 0
    value = ''
    def __init__(self, value='', type = Modify.Add):
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
        modifyers = []
        if self.channel.value != '':
            modifyers.append('ch%s'%(self.channel.toString()))
        if self.status.value != '':
            modifyers.append('st%s'%(self.status.toString()))
        if self.data1.value != '':
            modifyers.append('dt1%s'%(self.data1.toString()))
        if self.data2.value != '':
            modifyers.append('dt2%s'%(self.data2.toString()))

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