__author__ = 'prian'

from PyQt4.QtGui import QLineEdit, QKeyEvent
from PyQt4.QtCore import *
class KeysEdit( QLineEdit):
    keyPressSignal = pyqtSignal( QKeyEvent )

    def __init__(self, parent = None):
        QLineEdit.__init__(self, parent)

    def keyPressEvent(self, event):
        self.keyPressSignal.emit( event )
        QLineEdit.keyPressEvent(self, event)
  