from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QPainter, QColor
from gui import Ui_MainWindow
import sys


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
            self.pixmap = QPixmap(fileName)
            self.pixmap = self.pixmap.scaled(int(128), int(128), QtCore.Qt.KeepAspectRatio)
            self.highlight = QPainter()
            self.highlight.begin(self.pixmap)
            self.highlight.setCompositionMode(QPainter.CompositionMode_ColorDodge);
            self.highlight.fillRect(0,0,100,100, QColor(180, 180, 180, 100));
            self.ui.lblPhantom.setPixmap(self.pixmap)
            self.highlight.end()

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
