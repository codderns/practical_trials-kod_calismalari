# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kronometre.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QEventLoop
import time

class Ui_Form(object):

    def __init__(self):


        super().__init__()
    
        self.veriler()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 30, 351, 241))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.saatdeger = QtWidgets.QSpinBox(self.widget)
        self.saatdeger.setGeometry(QtCore.QRect(90, 110, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.saatdeger.setFont(font)
        self.saatdeger.setObjectName("saatdeger")
        self.dakikadeger = QtWidgets.QSpinBox(self.widget)
        self.dakikadeger.setGeometry(QtCore.QRect(180, 110, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.dakikadeger.setFont(font)
        self.dakikadeger.setObjectName("dakikadeger")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(100, 190, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 190, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 190, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.saat = QtWidgets.QLCDNumber(self.widget)
        self.saat.setGeometry(QtCore.QRect(70, 50, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.saat.setFont(font)
        self.saat.setObjectName("saat")
        self.dakikalcd = QtWidgets.QLCDNumber(self.widget)
        self.dakikalcd.setGeometry(QtCore.QRect(160, 50, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dakikalcd.setFont(font)
        self.dakikalcd.setObjectName("dakika")
        self.saatlabel = QtWidgets.QLabel(self.widget)
        self.saatlabel.setGeometry(QtCore.QRect(10, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.saatlabel.setFont(font)
        self.saatlabel.setText("")
        self.saatlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.saatlabel.setObjectName("saatlabel")
        self.dakikalabel = QtWidgets.QLabel(self.widget)
        self.dakikalabel.setGeometry(QtCore.QRect(190, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dakikalabel.setFont(font)
        self.dakikalabel.setText("")
        self.dakikalabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dakikalabel.setObjectName("dakikalabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.baslat)
        self.pushButton_2.clicked.connect(self.durdur)
        self.pushButton_3.clicked.connect(self.supur)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "BAŞLAT"))
        self.pushButton_2.setText(_translate("Form", "DURDUR"))
        self.pushButton_3.setText(_translate("Form", "SÜPÜR"))


    def veriler(self):
        self.loop = QEventLoop()
        self.saniyetoplam = 0
        self.dakika = 0
        self.sayac = 0
        self.saniye = 0
    def baslat(self):

        if(self.sayac != 0):
            self.dakika = int(self.saat.value())
            self.saniye = int(self.dakikalcd.value())

        if(self.sayac == 0):
            self.dakika = int(self.saatdeger.value())
            self.saniye = int(self.dakikadeger.value())

        self.sayac+=1

        self.saniyetoplam = self.dakika*60 + self.saniye

        while(self.saniyetoplam >=1 ):
            if(self.saniyetoplam % 60 == 0):
                self.dakika -=1
            if(self.saniye <= 0):
                self.saniye = 60
            self.saniyetoplam -= 1
            self.saniye -= 1
            if(self.saniyetoplam == 0):
                self.saat.display(0)
                self.dakikalcd.display(0)
                # print("{} dakika\n{} saniye".format(0,0))
            else:
                self.saat.display(self.dakika)
                self.dakikalcd.display(self.saniye)
                # print("{} dakika\n{} saniye".format(self.dakika,self.saniye))
            
            if(self.saniyetoplam == 0):
                self.sayac = 0
                
            self.loop = QEventLoop()
            QTimer.singleShot(1000, self.loop.quit)
            self.loop.exec_()

            

        
    def durdur(self):
        try:
            self.saniyetoplam = 0
        except:
            self.saatlabel.setText("Hata Oluştu")

    def supur(self):
        try:
            self.saniyetoplam = 0
            self.dakika = 0
            self.sayac = 0
            self.saniye = 0
            self.dakikalcd.display(0)
            self.saat.display(0)
         
            # self.baslat()
            
        except:
            self.saatlabel.setText("Hata Oluştu")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
