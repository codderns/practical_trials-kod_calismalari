from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QEventLoop
import time
import random

class Ui_Form(object):

    def __init__(self):
    

         super().__init__()
    
         self.veriler()    

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(529, 438)
        self.sayideger = QtWidgets.QLineEdit(Form)
        self.sayideger.setGeometry(QtCore.QRect(340, 160, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.sayideger.setFont(font)
        self.sayideger.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sayideger.setReadOnly(True)
        self.sayideger.setObjectName("sayideger")
        self.bilgiverme = QtWidgets.QLineEdit(Form)
        self.bilgiverme.setGeometry(QtCore.QRect(50, 50, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bilgiverme.setFont(font)
        self.bilgiverme.setReadOnly(True)
        self.bilgiverme.setObjectName("bilgiverme")
        self.giris = QtWidgets.QTextEdit(Form)
        self.giris.setGeometry(QtCore.QRect(50, 160, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.giris.setFont(font)
        self.giris.setObjectName("giris")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 110, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 165, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(85, 210, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_4.clicked.connect(self.baslat)
        self.pushButton_2.clicked.connect(self.hayir)
        self.pushButton.clicked.connect(self.evet)
        self.pushButton_3.clicked.connect(self.gir)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Number Guessing Game"))
        self.sayideger.setText(_translate("Form", "Remaining 7"))
        self.bilgiverme.setText(_translate("Form", "Guess a Number Between 0-400"))
        self.pushButton.setText(_translate("Form", "YES"))
        self.pushButton_2.setText(_translate("Form", "NO"))
        self.pushButton_3.setText(_translate("Form", "ENTER"))
        self.pushButton_4.setText(_translate("Form","Start Over"))

    def veriler(self):
        self.sayac = 7
        self.yenisayi = random.randint(0,400)
    def baslat(self):
        self.pushButton_4.show()
        self.sayac = 7
        self.sayideger.setText('Remaining: 7')
        self.bilgiverme.setText('Guess a Number Between 0-400')
        self.yenisayi = random.randint(0,400)
        
        self.pushButton.close()
        self.pushButton_2.close()
        
    def gir(self):

        self.sayac = self.sayac - 1
        
        try:

            deger = int(self.giris.toPlainText())
            #print(self.sayac)
            #print(self.yenisayi)
            #print(deger)

            
            if(self.yenisayi == deger):
                self.bilgiverme.setText("Great, Your Number: {} Play Again?".format(deger))
                self.sayideger.setText("Remaining: {}".format(self.sayac))
                self.pushButton.show()
                self.pushButton_2.show()
                self.pushButton_4.close()
                self.pushButton_3.close()
                self.sayac += 7 #In the last right, the counter has been increased so that the last if loop does not run on consciousness.
                            
            if(self.yenisayi < deger):
                self.bilgiverme.setText('Not! Estimate by Decreasing the Number')
                self.sayideger.setText("Remaining: {}".format(self.sayac))
                self.pushButton.close()
                self.pushButton_2.close()
                self.pushButton_4.show()

            if(self.yenisayi > deger):
                self.bilgiverme.setText('Not! Estimate By Increasing the Number')
                self.sayideger.setText("Remaining: {}".format(self.sayac))
                self.pushButton.close()
                self.pushButton_2.close()
                self.pushButton_4.show()
                
            if (self.sayac <= 0):
                self.bilgiverme.setText('The Guess is Full, Answer:{} Play again? '.format(self.yenisayi))
                self.sayideger.setText("Remaining: {}".format(self.sayac))
                self.pushButton.show()
                self.pushButton_2.show()
                self.pushButton_4.close()
                self.pushButton_3.close()
            
            
        except:
            self.bilgiverme.setText('Just Enter Number')
            self.sayac += 1
               
            self.loop = QEventLoop()
            QTimer.singleShot(2000, self.loop.quit)
            self.loop.exec_()
            self.bilgiverme.setText('Guess a Number Between 0-400')

        
        

    def evet(self):
        self.pushButton_3.show()
        self.baslat()
    def hayir(self):
        quit()
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
