'''
Created on 28.06.2011

@author: prian
'''
if __name__ == '__main__':
    from gui.MainWindow import MainWindow
    from PyQt4 import QtGui
    from PyQt4 import QtCore
    import sys
    from Settings import Settings
    
    app = QtGui.QApplication(sys.argv)
    wnd = MainWindow()
    wnd.setSettings(Settings())
    wnd.show()
    
    app.connect(app, QtCore.SIGNAL('closeAllWindows()'), app, QtCore.SLOT('exit'))
    app.exec_()
    
