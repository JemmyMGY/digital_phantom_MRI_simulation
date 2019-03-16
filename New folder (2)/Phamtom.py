# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Phantoms.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1003, 712)
        self.PhantomSize = QtWidgets.QComboBox(Form)
        self.PhantomSize.setGeometry(QtCore.QRect(660, 40, 73, 22))
        self.PhantomSize.setObjectName("PhantomSize")
        self.TissueProperty = QtWidgets.QComboBox(Form)
        self.TissueProperty.setGeometry(QtCore.QRect(820, 40, 73, 22))
        self.TissueProperty.setObjectName("TissueProperty")
        self.Image = QtWidgets.QLabel(Form)
        self.Image.setGeometry(QtCore.QRect(510, 240, 331, 301))
        self.Image.setObjectName("Image")
        self.TE = QtWidgets.QSpinBox(Form)
        self.TE.setGeometry(QtCore.QRect(870, 250, 42, 22))
        self.TE.setObjectName("TE")
        self.TR = QtWidgets.QSpinBox(Form)
        self.TR.setGeometry(QtCore.QRect(870, 330, 42, 22))
        self.TR.setObjectName("TR")
        self.FlipAngle = QtWidgets.QSpinBox(Form)
        self.FlipAngle.setGeometry(QtCore.QRect(870, 420, 42, 22))
        self.FlipAngle.setObjectName("FlipAngle")
        self.TimeSpan = QtWidgets.QSpinBox(Form)
        self.TimeSpan.setGeometry(QtCore.QRect(870, 500, 42, 22))
        self.TimeSpan.setObjectName("TimeSpan")
        self.Browse = QtWidgets.QPushButton(Form)
        self.Browse.setGeometry(QtCore.QRect(50, 30, 93, 28))
        self.Browse.setObjectName("Browse")
        self.Recoverygraph = QtWidgets.QGraphicsView(Form)
        self.Recoverygraph.setGeometry(QtCore.QRect(20, 120, 401, 261))
        self.Recoverygraph.setObjectName("Recoverygraph")
        self.Decaygraph = QtWidgets.QGraphicsView(Form)
        self.Decaygraph.setGeometry(QtCore.QRect(20, 420, 401, 271))
        self.Decaygraph.setObjectName("Decaygraph")
        self.PlotDecay = QtWidgets.QPushButton(Form)
        self.PlotDecay.setGeometry(QtCore.QRect(470, 660, 93, 28))
        self.PlotDecay.setObjectName("PlotDecay")
        self.PlotRecovery = QtWidgets.QPushButton(Form)
        self.PlotRecovery.setGeometry(QtCore.QRect(470, 600, 93, 28))
        self.PlotRecovery.setObjectName("PlotRecovery")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Image.setText(_translate("Form", "TextLabel"))
        self.Browse.setText(_translate("Form", "Browse"))
        self.PlotDecay.setText(_translate("Form", "Plot Decay"))
        self.PlotRecovery.setText(_translate("Form", "Plot Recovery"))

