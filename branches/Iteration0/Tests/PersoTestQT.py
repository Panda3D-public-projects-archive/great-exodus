'''
Created on 19 avr. 2011

@author: JD219546
'''

import sys
import time

from PyQt4 import QtGui
from PyQt4 import QtCore

# Global variable used as a quick and dirty way to notify my
# main event loop that the MainWindow has been exited
APP_RUNNING = False

class SampleMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        global APP_RUNNING
        APP_RUNNING = True

        # main window
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Test')
        self.statusBar().showMessage('Ready')

        # exit action (assumes that the exit icon from
        # http://upload.wikimedia.org/wikipedia/commons/b/bc/Exit.png
        # is saved as Exit.png in the same folder as this file)
        exitAction = QtGui.QAction(QtGui.QIcon('Exit.png')
                                   ,'Exit'
                                   ,self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        self.connect(exitAction
                     ,QtCore.SIGNAL('triggered()')
                     ,QtCore.SLOT('close()'))

        # main menu
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        # toolbar
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        # text editor
        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)

        #tool tip
        textEdit.setToolTip('Enter some text')
        QtGui.QToolTip.setFont(QtGui.QFont('English', 12))

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self
                                           ,'Message'
                                           ,"Are you sure?"
                                           ,QtGui.QMessageBox.Yes
                                           ,QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
            global APP_RUNNING
            APP_RUNNING = False
        else:
            event.ignore()
if __name__ == '__main__':
    
    
    # main program
    app = QtGui.QApplication(sys.argv)
    testWindow = SampleMainWindow()
    testWindow.show()
    # run custom event loop instead of app.exec_()
    i = 0
    while APP_RUNNING:
        i += 1
        print("Iteration",i)
        app.processEvents()
        # sleep to prevent that my "great" event loop eats 100% cpu
        time.sleep(0.04)
        pass