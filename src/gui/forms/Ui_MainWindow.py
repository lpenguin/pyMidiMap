# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/prian/workspace/pyMidiMap/src/gui/forms/MainWindow.ui'
#
# Created: Tue Jul  5 17:08:11 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(838, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.addButton = QtGui.QPushButton(self.centralwidget)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.horizontalLayout.addWidget(self.addButton)
        self.editButton = QtGui.QPushButton(self.centralwidget)
        self.editButton.setObjectName(_fromUtf8("editButton"))
        self.horizontalLayout.addWidget(self.editButton)
        self.removeButton = QtGui.QPushButton(self.centralwidget)
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.horizontalLayout.addWidget(self.removeButton)
        self.duplicateButton = QtGui.QPushButton(self.centralwidget)
        self.duplicateButton.setObjectName(_fromUtf8("duplicateButton"))
        self.horizontalLayout.addWidget(self.duplicateButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.mapList = MidiMapTableWidget(self.centralwidget)
        self.mapList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.mapList.setRowCount(0)
        self.mapList.setColumnCount(2)
        self.mapList.setObjectName(_fromUtf8("mapList"))
        self.mapList.setColumnCount(2)
        self.mapList.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.mapList.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.mapList.setHorizontalHeaderItem(1, item)
        self.mapList.horizontalHeader().setCascadingSectionResizes(True)
        self.mapList.horizontalHeader().setDefaultSectionSize(200)
        self.mapList.horizontalHeader().setMinimumSectionSize(200)
        self.mapList.horizontalHeader().setStretchLastSection(True)
        self.mapList.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.mapList)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 838, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionMidi = QtGui.QAction(MainWindow)
        self.actionMidi.setObjectName(_fromUtf8("actionMidi"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionLog = QtGui.QAction(MainWindow)
        self.actionLog.setObjectName(_fromUtf8("actionLog"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_as = QtGui.QAction(MainWindow)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuSettings.addAction(self.actionMidi)
        self.menuView.addAction(self.actionLog)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.actionMidi, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.showMidiWindow)
        QtCore.QObject.connect(self.addButton, QtCore.SIGNAL(_fromUtf8("pressed()")), MainWindow.addMap)
        QtCore.QObject.connect(self.editButton, QtCore.SIGNAL(_fromUtf8("pressed()")), MainWindow.editMap)
        QtCore.QObject.connect(self.removeButton, QtCore.SIGNAL(_fromUtf8("pressed()")), MainWindow.removeMap)
        QtCore.QObject.connect(self.duplicateButton, QtCore.SIGNAL(_fromUtf8("pressed()")), MainWindow.duplicateMap)
        QtCore.QObject.connect(self.actionLog, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.showLog)
        QtCore.QObject.connect(self.actionOpen, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.openTriggered)
        QtCore.QObject.connect(self.actionSave, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.saveTriggered)
        QtCore.QObject.connect(self.actionSave_as, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.saveAsTriggered)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Midi Mapper", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Mappings", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.editButton.setText(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.removeButton.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.duplicateButton.setText(QtGui.QApplication.translate("MainWindow", "Duplicate", None, QtGui.QApplication.UnicodeUTF8))
        self.mapList.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Message", None, QtGui.QApplication.UnicodeUTF8))
        self.mapList.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Action", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setTitle(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMidi.setText(QtGui.QApplication.translate("MainWindow", "Midi Ports", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLog.setText(QtGui.QApplication.translate("MainWindow", "Log", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setText(QtGui.QApplication.translate("MainWindow", "Save as...", None, QtGui.QApplication.UnicodeUTF8))

from gui.MidiMapTableWidget import MidiMapTableWidget
