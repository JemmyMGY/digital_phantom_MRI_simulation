import sys
from random import randint
from PyQt5 import QtGui, QtWidgets, QtCore
from Phamtom import Ui_MainWindow
import numpy as np


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.PlotRecovery.clicked.connect(self.onClick1)
        self.ui.PlotDecay.clicked.connect(self.onClick2)
        self.draw = False
        self.ui.PlotRecovery.setCheckable(True)
        self.ui.PlotDecay.setCheckable(True)

    def onClick1(self):
        if self.ui.PlotRecovery.isChecked():
            self.draw = True
            self.plot()
        else:
            self.draw = False

    def onClick2(self):
        if self.ui.PlotDecay.isChecked():
            self.draw = True
            self.plot()
        else:
            self.draw = False


    def plot(self):
        arr1 = []
        # arr2 = []
        plotWindow = self.ui.Recoverygraph
        plotWindow.clear()
        # plot.showGrid(x=True, y=True, alpha=1)
        while self.draw:
            arr1.append(randint(0, 1000))
            # arr2.append(randint(0, 1000))
            plotWindow.plot(arr1)
            # plotWindow.plot(arr2, pen='r')
            # plotWindow.plot(arr1, arr2, pen='y')
            QtGui.QApplication.processEvents()

        # print('arr1[0]', arr1[0])
        # print('arr2[0]', arr2[0])


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
