# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis, QValueAxis
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

xAxis = ["a", "b", "c", "d", "e", "f"]
yAxis = [1,2,3,4,5,6]



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 400)
        self.LengthInput = QtWidgets.QLineEdit(Dialog)
        self.LengthInput.setGeometry(QtCore.QRect(370, 130, 113, 20))
        self.LengthInput.setAlignment(QtCore.Qt.AlignCenter)
        self.LengthInput.setObjectName("LengthInput")
        self.ImpedanceInput = QtWidgets.QLineEdit(Dialog)
        self.ImpedanceInput.setGeometry(QtCore.QRect(370, 80, 113, 20))
        self.ImpedanceInput.setAlignment(QtCore.Qt.AlignCenter)
        self.ImpedanceInput.setObjectName("ImpedanceInput")
        self.WelcomeButton = QtWidgets.QPushButton(Dialog)
        self.WelcomeButton.setGeometry(QtCore.QRect(300, 320, 111, 51))
        self.WelcomeButton.setObjectName("WelcomeButton")
        self.Impedancelabel = QtWidgets.QLabel(Dialog)
        self.Impedancelabel.setGeometry(QtCore.QRect(40, 60, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Impedancelabel.setFont(font)
        self.Impedancelabel.setScaledContents(False)
        self.Impedancelabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Impedancelabel.setWordWrap(False)
        self.Impedancelabel.setObjectName("Impedancelabel")
        self.Lengthlabel = QtWidgets.QLabel(Dialog)
        self.Lengthlabel.setGeometry(QtCore.QRect(40, 110, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Lengthlabel.setFont(font)
        self.Lengthlabel.setScaledContents(False)
        self.Lengthlabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Lengthlabel.setWordWrap(False)
        self.Lengthlabel.setObjectName("Lengthlabel")
        self.NextButton = QtWidgets.QPushButton(Dialog)
        self.NextButton.setGeometry(QtCore.QRect(300, 250, 111, 51))
        self.NextButton.setObjectName("NextButton")

        
        self.create_bar()



        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.WelcomeButton.setText(_translate("Dialog", "Welcome"))
        self.Impedancelabel.setText(_translate("Dialog", "Enter impedance of section 1"))
        self.Lengthlabel.setText(_translate("Dialog", "Enter length of section 1"))
        self.NextButton.setText(_translate("Dialog", "Next"))

    def create_bar(self):
            global xAxis,yAxis
            #The QBarSet class represents a set of bars in the bar chart.
            # It groups several bars into a bar set

            set0 = QBarSet("Parwiz")


            #set0.append([1, 2, 3, 4, 5, 6])
            set0.append(yAxis)

            series = QBarSeries()
            series.append(set0)

            chart = QChart()
            chart.addSeries(series)
            chart.setTitle("Percent Example")
            chart.setAnimationOptions(QChart.SeriesAnimations)

            #categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
            categories= xAxis
            axis = QBarCategoryAxis()
            axis.append(categories)
            chart.createDefaultAxes()
            chart.setAxisX(axis, series)


            chart.legend().setVisible(True)
            chart.legend().setAlignment(Qt.AlignTop)

            #chart.setPos(300,200)

            chartView = QChartView(chart)
            chartView.setRenderHint(QPainter.Antialiasing)

            self.setCentralWidget(chartView)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())