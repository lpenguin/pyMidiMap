__author__ = 'prian'
import platform

windowsOS = 0 #Linux
if platform.system() == 'Windows':
    import _sendkeys
    windowsOS = 1

def SendKeyPress( vk ):
    SendKeyDown( vk )
    SendKeyUp( vk )

def SendKeyUp( vk ):
    if windowsOS:
        _sendkeys.key_up( vk )
    else:
        print "'KeyUp' Not realized on Linux yet"


def SendKeyDown( vk ):
    if windowsOS:
        _sendkeys.key_down( vk )
    else:
        print "'KeyDown' Not realized on Linux yet"