from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QPainter, QColor, QImage
from gui import Ui_MainWindow
import sys
import math
import numpy as np
import cv2
import properties
import kspace
import qimage2ndarray


class ApplicationWindow(QtWidgets.QMainWindow):
    resized = pyqtSignal()
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pbBrowse.clicked.connect(self.pbBrowse_clicked)
        self.ui.cbSize.currentTextChanged.connect(self.cbSize_currentTextChanged)
        self.ui.cbProperty.currentTextChanged.connect(self.cbProperty_currentTextChanged)
        self.ui.sbGraphs.valueChanged.connect(self.sbGraphs_valueChanged)
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
        '''
        self.plt = self.ui.gvDecay
        '''
        #y = [2,4,6,8,10,12,14,16,18,20]
        #h = [5,5,6,8,-10,-5,-14,4,8,-5]
        #x = range(0,10)
        #plt.setLabel('left', 'Value', units='V')
        #plt.setLabel('bottom', 'Time', units='s')
        #self.plt.setXRange(-100,100)
        #self.plt.setYRange(0,100)
        '''
        self.graph(lambda x: (np.exp(-x)), (0,10,0.01), self.plt)
        self.plt = self.ui.gvRecovery
        self.graph(lambda x: (1-(np.exp(-x))), (0,10,0.01), self.plt)
        '''
        #plt.plot(x, y, pen='w')
        #plt.plot(x, h, pen='b')
        self.fileName, _filter = QFileDialog.getOpenFileName(self, "Open", "", "Filter -- All Files (*);;Python Files (*.py)")
        self.ui.gvDecay.clear()
        self.ui.gvRecovery.clear()
        self.getPhantom()

    def getPhantom(self):
        try:
            if self.fileName:
                print(self.fileName)
                size = int(self.ui.cbSize.currentText())
                self.cvImg = cv2.imread(self.fileName,0)
                self.cvImg = cv2.resize(self.cvImg,(size,size))
                self.original = self.cvImg
                self.cvImgT1 = properties.t1(self.cvImg)
                self.cvImgT2 = properties.t2(self.cvImg)
                self.cvImgPD = properties.pd(self.cvImg)
                prop = self.ui.cbProperty.currentText()
                if prop=='T1':
                    self.cvImg = self.cvImgT1
                elif prop=='T2':
                    self.cvImg = self.cvImgT2
                elif prop=='PD':
                    self.cvImg = self.cvImgPD
                print(type(self.cvImg))
                #self.rfPulse()
                self.displayPhantom(self.cvImg)
                QtWidgets.QApplication.processEvents()
        except:
            pass
        
    def rfPulse(self):
        te = self.ui.sbTE.value()
        tr = self.ui.sbTR.value()
        fa = self.ui.sbFA.value()
        t1 = cv2.resize(self.cvImgT1,(64,64))
        t2 = cv2.resize(self.cvImgT2,(64,64))
        pd = cv2.resize(self.cvImgPD,(64,64))
        QtWidgets.QApplication.processEvents()
        image = kspace.flip(te, tr, t1, t2, pd, fa)
        qimg = QImage()
        qimg = qimage2ndarray.array2qimage(image)
        pix = QPixmap(qimg)
        self.ui.lblImage.setPixmap(pix)
        

    def displayPhantom(self, image):
        try:
            self.highlight.end()
        except:
            pass
        #height, width, channel = cvImg.shape
        #bytesPerLine = 3 * size
        size = int(self.ui.cbSize.currentText())
        self.img = QImage(image.data, size, size, QImage.Format_Grayscale8)
        #self.img = QImage(fileName)
        self.pixmap = QPixmap(self.img)
        self.pixmap = self.pixmap.scaled(size, size, QtCore.Qt.KeepAspectRatio)
        self.ui.lblPhantom.setPixmap(self.pixmap)
        self.highlight = QPainter()
        self.highlight.begin(self.pixmap)
        self.position = [[0]*2]*5
        self.number = 0
        self.ui.lblPhantom.mousePressEvent = self.getPos
        self.ui.lblPhantom.mouseWheelEvent = self.wheelEvent

    def cbSize_currentTextChanged(self, value):
        value = int(value)
        if(value==128):
            self.setMinimumSize(450,450)
            self.resize(450,450)
        elif(value==256):
            self.setMinimumSize(727,578)
            self.resize(727,578)
        else:
            self.setMinimumSize(1238,834)
            self.resize(1238,834)
        self.ui.gvDecay.clear()
        self.ui.gvRecovery.clear()
        self.getPhantom()

    def cbProperty_currentTextChanged(self, value):
        try:
            if value=='T1':
                self.cvImg = self.cvImgT1
            elif value=='T2':
                self.cvImg = self.cvImgT2
            elif value=='PD':
                self.cvImg = self.cvImgPD
            else:
                self.cvImg = self.original
            self.displayPhantom(self.cvImg)
        except:
            pass

    def sbGraphs_valueChanged(self, value):
        self.ui.gvDecay.setXRange(0,value)
        self.ui.gvRecovery.setXRange(0,value)

    def getPos(self , event):
        size = int(self.ui.cbSize.currentText())
        x = math.floor(event.pos().x()*size/self.ui.lblPhantom.frameGeometry().width())
        y = math.floor(event.pos().y()*size/self.ui.lblPhantom.frameGeometry().height())
        t1 = self.cvImgT1[y][x]
        t2 = self.cvImgT2[y][x]
        print('t1:',t1,' ','t2:',t2)
        fa = np.deg2rad(self.ui.sbFA.value())
        color = [QColor(0, 0, 255, 75), QColor(0, 255, 0, 75), QColor(255, 0, 0, 75), QColor(255, 0, 255, 75), QColor(255, 255, 0, 75)]
        if self.number%5==0:
            print('1')
            self.highlight.end()
            self.ui.lblPhantom.clear()
            self.pixmap = QPixmap(self.img)
            self.pixmap = self.pixmap.scaled(size, size, QtCore.Qt.KeepAspectRatio)
            self.highlight.begin(self.pixmap)
            self.ui.gvDecay.clear()
            self.ui.gvRecovery.clear()
        self.position[self.number%5]=[x,y]
        print(x,'x',y)
        self.highlight.fillRect(self.position[self.number%5][0],self.position[self.number%5][1],10,10, color[self.number%5])
        self.ui.lblPhantom.setPixmap(self.pixmap)
        self.plt = self.ui.gvDecay
        self.graph(lambda x: (np.exp(-x/t2)*(np.sin(fa))), (0,10000,0.01), self.plt)
        self.plt = self.ui.gvRecovery
        self.graph(lambda x: (np.exp(-x/t1)*((np.cos(fa))-1)+1), (0,10000,0.01), self.plt)
        self.number += 1

    def graph(self, func, x_range, plt):
        x = np.arange(*x_range)
        y = func(x)
        span = self.ui.sbGraphs.value()
        color = ['b', 'g', 'r', 'm', 'y']
        self.plt.plot(x, y, pen=color[self.number%5])
        self.plt.setXRange(0,span)

    def winResize(self):
        #print('resize');
        print('label:',self.ui.lblPhantom.frameGeometry().width(), 'x', self.ui.lblPhantom.frameGeometry().height())
        print('Window:',self.frameGeometry().width(), 'x', self.frameGeometry().height())
        '''scale = self.frameGeometry().height()-400+128
        try:
            self.pixmap = self.pixmap.scaled(int(scale), int(scale), QtCore.Qt.KeepAspectRatio)
            self.ui.label.setPixmap(self.pixmap)
        except:
            pass'''

    def wheelEvent(self, event):
        image = self.cvImg
        increaseFactor = 10
        decreaseFactor = -10
        if event.angleDelta().y() > 0:
            for i in range(image.shape[0]):
                for j in range(image.shape[1]):
                    if image[i][j] < 245:
                        image[i][j] = image[i][j] + increaseFactor
        else:
            for i in range(image.shape[0]):
                for j in range(image.shape[1]):
                    if image[i][j] > 10:
                        image[i][j] = image[i][j] - decreaseFactor
        self.displayPhantom(image)

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
