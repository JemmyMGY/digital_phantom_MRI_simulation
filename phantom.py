from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QPainter, QColor, QImage
from gui import Ui_MainWindow
import sys
import math


class ApplicationWindow(QtWidgets.QMainWindow):
    resized = pyqtSignal();
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pbBrowse.clicked.connect(self.pbBrowse_clicked)
        self.resized.connect(self.winResize)

    def resizeEvent(self, event):
        self.resized.emit()
        #super(ApplicationWindow, self).resize(700,700)
        '''if self.frameGeometry().width()>self.frameGeometry().height():
            self.resize(self.frameGeometry().width(),self.frameGeometry().width())
        elif self.frameGeometry().width()<self.frameGeometry().height():
            self.resize(self.frameGeometry().height(),self.frameGeometry().height())'''
        return super(ApplicationWindow, self).resizeEvent(event)

    def pbBrowse_clicked(self):
        #self.resize(700,700)
        fileName, _filter = QFileDialog.getOpenFileName(self, "Open", "", "Filter -- All Files (*);;Python Files (*.py)")
        if fileName:
            try:
                self.highlight.end()
            except:
                pass
            self.img = QImage(fileName)
            self.pixmap = QPixmap(self.img)
            self.pixmap = self.pixmap.scaled(int(128), int(128), QtCore.Qt.KeepAspectRatio)
            self.ui.lblPhantom.setPixmap(self.pixmap)
            self.highlight = QPainter()
            self.highlight.begin(self.pixmap)
            self.position = [[0]*2]*5
            self.number = 0
            self.ui.lblPhantom.mousePressEvent = self.getPos

    def getPos(self , event):
        x = math.floor(event.pos().x()*128/self.ui.lblPhantom.frameGeometry().width())
        y = math.floor(event.pos().y()*128/self.ui.lblPhantom.frameGeometry().height())
        color = [QColor(0, 0, 255, 75), QColor(0, 255, 0, 75), QColor(255, 0, 0, 75), QColor(255, 0, 255, 75), QColor(255, 255, 0, 75)]
        if self.number%5==0:
            print('1')
            self.highlight.end()
            self.ui.lblPhantom.clear()
            self.pixmap = QPixmap(self.img)
            self.pixmap = self.pixmap.scaled(int(128), int(128), QtCore.Qt.KeepAspectRatio)
            self.highlight.begin(self.pixmap)
        self.position[self.number%5]=[x,y]
        print(x,'x',y)
        self.highlight.fillRect(self.position[self.number%5][0],self.position[self.number%5][1],10,10, color[self.number%5])
        self.ui.lblPhantom.setPixmap(self.pixmap)
        self.number += 1

    def winResize(self):
        #print('resize');
        print(self.ui.lblPhantom.frameGeometry().width(), 'x', self.ui.lblPhantom.frameGeometry().height())
        '''scale = self.frameGeometry().height()-400+128
        try:
            self.pixmap = self.pixmap.scaled(int(scale), int(scale), QtCore.Qt.KeepAspectRatio)
            self.ui.label.setPixmap(self.pixmap)
        except:
            pass'''


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
