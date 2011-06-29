__author__ = 'prian'

from PyQt4.QtGui import QDialog
from forms.Ui_LogDialog import Ui_LogDialog
from classes.Settings import Settings

class LogDialog(QDialog, Ui_LogDialog):
    settings = Settings()

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)