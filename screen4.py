# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen4.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 400)
        self.JunctionNumInput = QtWidgets.QLineEdit(Dialog)
        self.JunctionNumInput.setGeometry(QtCore.QRect(320, 110, 113, 20))
        self.JunctionNumInput.setObjectName("JunctionNumInput")
        self.JunctionNunLabel = QtWidgets.QLabel(Dialog)
        self.JunctionNunLabel.setGeometry(QtCore.QRect(150, 110, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.JunctionNunLabel.setFont(font)
        self.JunctionNunLabel.setObjectName("JunctionNunLabel")
        self.IterationsNumInput = QtWidgets.QLineEdit(Dialog)
        self.IterationsNumInput.setGeometry(QtCore.QRect(320, 140, 113, 20))
        self.IterationsNumInput.setObjectName("IterationsNumInput")
        self.IterationsNumLabel = QtWidgets.QLabel(Dialog)
        self.IterationsNumLabel.setGeometry(QtCore.QRect(150, 140, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.IterationsNumLabel.setFont(font)
        self.IterationsNumLabel.setObjectName("IterationsNumLabel")
        self.DisplayButton = QtWidgets.QPushButton(Dialog)
        self.DisplayButton.setGeometry(QtCore.QRect(230, 200, 131, 41))
        self.DisplayButton.setObjectName("DisplayButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.JunctionNunLabel.setText(_translate("Dialog", "Junction number"))
        self.IterationsNumLabel.setText(_translate("Dialog", "Number of iterations"))
        self.DisplayButton.setText(_translate("Dialog", "Display"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
