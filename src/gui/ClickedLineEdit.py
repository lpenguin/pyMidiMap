__author__ = 'prian'
from PyQt4.QtCore import *
from PyQt4.QtGui import QLineEdit

class ClickedLineEdit (QLineEdit):
    clicked = pyqtSignal( )
    def __init__(self, parent = None):
        QLineEdit.__init__(self, parent)

    def mousePressEvent(self, event):
        self.clicked.emit()
        QLineEdit.mousePressEvent(self, event)