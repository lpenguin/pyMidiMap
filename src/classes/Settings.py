'''
Created on 28.06.2011

@author: prian
'''
import rtmidi

class Settings(object):
    
    midiIn = rtmidi.RtMidiIn()
    midiOut = rtmidi.RtMidiOut()
    midiInPort = None
    midiOutPort = None
    
    def __init__(self):
        pass
        