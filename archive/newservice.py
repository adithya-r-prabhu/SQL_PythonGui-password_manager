# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'temp/newservice.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from listview import *
from sql import *


class newserviceclass(object):
    def newservicewindow(self, Dialog):
        self.MainWindow = Dialog

        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 732)
        self.addnewservicelabel = QtWidgets.QLabel(Dialog)
        self.addnewservicelabel.setGeometry(QtCore.QRect(50, 0, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.addnewservicelabel.setFont(font)
        self.addnewservicelabel.setObjectName("addnewservicelabel")
        self.servicenamelineEdit = QtWidgets.QLineEdit(Dialog)
        self.servicenamelineEdit.setGeometry(QtCore.QRect(10, 150, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.servicenamelineEdit.setFont(font)
        self.servicenamelineEdit.setText("")
        self.servicenamelineEdit.setObjectName("servicenamelineEdit")
        self.usernamelineedit = QtWidgets.QLineEdit(Dialog)
        self.usernamelineedit.setGeometry(QtCore.QRect(10, 260, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.usernamelineedit.setFont(font)
        self.usernamelineedit.setText("")
        self.usernamelineedit.setObjectName("usernamelineedit")
        self.passwordlineedit = QtWidgets.QLineEdit(Dialog)
        self.passwordlineedit.setGeometry(QtCore.QRect(10, 390, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.passwordlineedit.setFont(font)
        self.passwordlineedit.setText("")
        self.passwordlineedit.setObjectName("passwordlineedit")
        self.savebutton = QtWidgets.QPushButton(Dialog)
        self.savebutton.setGeometry(QtCore.QRect(10, 510, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.savebutton.setFont(font)
        self.savebutton.setObjectName("savebutton")
        self.servicenamelabel = QtWidgets.QLabel(Dialog)
        self.servicenamelabel.setGeometry(QtCore.QRect(20, 100, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.servicenamelabel.setFont(font)
        self.servicenamelabel.setObjectName("servicenamelabel")
        self.usernamelabel = QtWidgets.QLabel(Dialog)
        self.usernamelabel.setGeometry(QtCore.QRect(20, 210, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.usernamelabel.setFont(font)
        self.usernamelabel.setObjectName("usernamelabel")
        self.passwordlabel = QtWidgets.QLabel(Dialog)
        self.passwordlabel.setGeometry(QtCore.QRect(20, 340, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.passwordlabel.setFont(font)
        self.passwordlabel.setObjectName("passwordlabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.savebutton.clicked.connect(
            self.onclicksavebutton
        ) 

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "addnewservice"))
        self.addnewservicelabel.setText(_translate("Dialog", "Add   New   Service"))
        self.savebutton.setText(_translate("Dialog", "Save"))
        self.servicenamelabel.setText(_translate("Dialog", "Service_name(eg. Amazon,Google)"))
        self.usernamelabel.setText(_translate("Dialog", "Username"))
        self.passwordlabel.setText(_translate("Dialog", "Password"))

    global listview
    def listview(self):
        self.MainWindow.close()

        self.window = QtWidgets.QMainWindow()
        self.ui = listviewclass()
        self.ui.listviewwindow(self.window)
        self.window.show()
    def onclicksavebutton(self):
        servicename=self.servicenamelineEdit.text()
        username=self.usernamelineedit.text()
        password=self.passwordlineedit.text()
        command="select * from services;"
        l=database(command,getoutput=True)
        if (servicename,username,password) not in l:
            command="insert into services values('"+servicename+"','"+username+"','"+password+"');"
            database(command)
        listview(self)




        
        

    



# if __name__ == "__main__":

#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = newserviceclass()
#     ui.newservicewindow(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())