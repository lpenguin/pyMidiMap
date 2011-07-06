from PyQt4.QtCore import QStringList

__author__ = 'prian'
__maps = []
from PyQt4.QtGui import QTableWidget
from PyQt4.QtGui import QTableWidgetItem

class MidiMapTableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)
        self.__maps = []
        #self.setupUi()

    #def setupUi(self):
    #    self.setRowCount(1)
    #    self.setColumnCount(2)
    #    self.setVerticalHeaderLabels( QStringList(['message', 'action']))

    def addMidiMap(self, map):
        self.__maps.append(map)
        row = self.rowCount()
        self.insertRow(row)
    
        self.setItem(row, 0, QTableWidgetItem(map.message.toString()))
        self.setItem(row, 1, QTableWidgetItem(map.action.toString()))
        self.resizeRowsToContents()

        if not len( self.selectedIndexes() ):
            self.selectRow( 0 )


    def removeMidiMap(self, index):
        if( index < len(self.__maps)):
            self.__maps.pop(index)
            self.removeRow(index)
           # self.emit(SIGNAL('dataChanged'))

    def setMidiMap(self, index, map):
        if( index < len(self.__maps)):
            self.__maps[index] = map
            self.setItem(index, 0, QTableWidgetItem(map.message.toString()))
            self.setItem(index, 1, QTableWidgetItem(map.action.toString()))
            #self.emit(SIGNAL('dataChanged'))

    def getMidiMap(self, index):
          if( index < len(self.__maps)):
             return  self.__maps[index]

    def maps(self):
        return self.__maps

    def setMaps(self, maps):
        self.__maps = []
        for i in range(len(self.__maps)):
            self.removeMidiMap(0)
        for map in maps:
            self.addMidiMap(map)