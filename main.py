from PyQt5 import QtCore, QtGui, QtWidgets
import pyperclip


from alert import *
from sql import *
from generate_random_password import *
#importing functions from files

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.MainWindow = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(523, 626)
        Dialog.setStyleSheet("")
        self.welcomelabel = QtWidgets.QLabel(Dialog)
        self.welcomelabel.setGeometry(QtCore.QRect(20, 10, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.welcomelabel.setFont(font)
        self.welcomelabel.setObjectName("welcomelabel")
        self.headinglabel = QtWidgets.QLabel(Dialog)
        self.headinglabel.setGeometry(QtCore.QRect(60, 70, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.headinglabel.setFont(font)
        self.headinglabel.setAutoFillBackground(True)
        self.headinglabel.setObjectName("headinglabel")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(200, 150, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.usernamelabel = QtWidgets.QLabel(Dialog)
        self.usernamelabel.setGeometry(QtCore.QRect(80, 259, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.usernamelabel.setFont(font)
        self.usernamelabel.setObjectName("usernamelabel")
        self.usernamelineedit = QtWidgets.QLineEdit(Dialog)
        self.usernamelineedit.setGeometry(QtCore.QRect(190, 260, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.usernamelineedit.setFont(font)
        self.usernamelineedit.setObjectName("usernamelineedit")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 560, 541, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.loginpushbutton = QtWidgets.QPushButton(Dialog)
        self.loginpushbutton.setGeometry(QtCore.QRect(280, 390, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loginpushbutton.setFont(font)
        self.loginpushbutton.setObjectName("loginpushbutton")
        self.passworlabel = QtWidgets.QLabel(Dialog)
        self.passworlabel.setGeometry(QtCore.QRect(80, 309, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passworlabel.setFont(font)
        self.passworlabel.setObjectName("passworlabel")
        self.passwordlineedit = QtWidgets.QLineEdit(Dialog)
        self.passwordlineedit.setGeometry(QtCore.QRect(190, 310, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passwordlineedit.setFont(font)
        self.passwordlineedit.setObjectName("passwordlineedit")
        self.extrathingsframe = QtWidgets.QFrame(Dialog)
        self.extrathingsframe.setGeometry(QtCore.QRect(0, 570, 521, 51))
        self.extrathingsframe.setStyleSheet("")
        self.extrathingsframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.extrathingsframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.extrathingsframe.setLineWidth(0)
        self.extrathingsframe.setObjectName("extrathingsframe")
        self.contactuspussbutton = QtWidgets.QPushButton(self.extrathingsframe)
        self.contactuspussbutton.setGeometry(QtCore.QRect(380, 10, 80, 25))
        self.contactuspussbutton.setObjectName("contactuspussbutton")
        self.twitterpushbutton = QtWidgets.QPushButton(self.extrathingsframe)
        self.twitterpushbutton.setGeometry(QtCore.QRect(260, 10, 80, 25))
        self.twitterpushbutton.setObjectName("twitterpushbutton")
        self.helpbutton = QtWidgets.QPushButton(self.extrathingsframe)
        self.helpbutton.setGeometry(QtCore.QRect(20, 10, 80, 25))
        self.helpbutton.setObjectName("helpbutton")
        self.websitpushbutton = QtWidgets.QPushButton(self.extrathingsframe)
        self.websitpushbutton.setGeometry(QtCore.QRect(130, 10, 80, 25))
        self.websitpushbutton.setObjectName("websitpushbutton")
        self.registercheckbox = QtWidgets.QCheckBox(Dialog)
        self.registercheckbox.setGeometry(QtCore.QRect(170, 390, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.registercheckbox.setFont(font)
        self.registercheckbox.setObjectName("registercheckbox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.loginpushbutton.clicked.connect(
            self.onclickloginpushbutton
        ) 


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.welcomelabel.setText(_translate("Dialog", "WELCOME To"))
        self.headinglabel.setText(_translate("Dialog", " Sarathi Password Manager"))
        self.label_3.setText(_translate("Dialog", "LOGIN"))
        self.usernamelabel.setText(_translate("Dialog", "USERNAME:"))
        self.loginpushbutton.setText(_translate("Dialog", "Login"))
        self.passworlabel.setText(_translate("Dialog", "PASSWORD:"))
        self.contactuspussbutton.setText(_translate("Dialog", "contact us"))
        self.twitterpushbutton.setText(_translate("Dialog", "twitter"))
        self.helpbutton.setText(_translate("Dialog", "help"))
        self.websitpushbutton.setText(_translate("Dialog", "website"))
        self.registercheckbox.setText(_translate("Dialog", "Register"))
   
    global alert
    def alert(self,alerttext):

        self.window = QtWidgets.QMainWindow()
        self.ui = alertclass()
        self.ui.alertwindow(self.window,alerttext)
        self.window.show()
    global listview
    def listview(self):
        self.MainWindow.close()

        self.window = QtWidgets.QMainWindow()
        self.ui = listviewclass()
        self.ui.listviewwindow(self.window)
        self.window.show()

  

    def onclickloginpushbutton(self):
        def login():
                global username
                username=self.usernamelineedit.text()
                password=self.passwordlineedit.text()
                command="select * from login;"
                l=database(command,getoutput=True)
                if (username,password) in l:
                    alert(self,"login successful")
                    listview(self)
                else:
                    alert(self,"pls register")

                    
        def register():
                username=self.usernamelineedit.text()
                password=self.passwordlineedit.text()
                #checking if that same username and password exist
                command="select * from login;"
                l=database(command,getoutput=True)
                if (username,password) not in l:
                    command="insert into login values('"+username+"','"+password+"');"
                    database(command)
                    login()
                else:
                    alert(self,"username and password already exist")

        
        if self.registercheckbox.isChecked()== True:
            register()
        else:
            login()

selected=[]

class edit_viewclass(object):
    
    def edit_viewwindow(self, Dialog):
        global selected
        self.MainWindow = Dialog

        Dialog.setObjectName("Dialog")
        Dialog.resize(421, 688)
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
        self.servicenamelineEdit.setGeometry(QtCore.QRect(10, 150, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.servicenamelineEdit.setFont(font)
        self.servicenamelineEdit.setText("")
        self.servicenamelineEdit.setObjectName("servicenamelineEdit")
        self.servicenamelineEdit.setText(selected[0]) 

        self.usernamelineedit = QtWidgets.QLineEdit(Dialog)
        self.usernamelineedit.setGeometry(QtCore.QRect(10, 260, 331, 51))
        self.usernamelineedit.setText(selected[1]) 
        font = QtGui.QFont()
        font.setPointSize(18)
        self.usernamelineedit.setFont(font)
        self.usernamelineedit.setObjectName("usernamelineedit")
        self.passwordlineedit = QtWidgets.QLineEdit(Dialog)
        self.passwordlineedit.setGeometry(QtCore.QRect(10, 390, 331, 51))
        self.passwordlineedit.setText(selected[2]) 

        font = QtGui.QFont()
        font.setPointSize(18)
        self.passwordlineedit.setFont(font)
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
        self.deletebutton = QtWidgets.QPushButton(Dialog)
        self.deletebutton.setGeometry(QtCore.QRect(10, 570, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deletebutton.setFont(font)
        self.deletebutton.setObjectName("deletebutton")
        self.usernamecopy = QtWidgets.QPushButton(Dialog)
        self.usernamecopy.setGeometry(QtCore.QRect(350, 260, 41, 51))
        self.usernamecopy.setObjectName("usernamecopy")
        self.passwordcopy = QtWidgets.QPushButton(Dialog)
        self.passwordcopy.setGeometry(QtCore.QRect(350, 390, 41, 51))
        self.passwordcopy.setObjectName("passwordcopy")

        self.savebutton.clicked.connect(
            self.onclicksavebutton
        ) 
        self.deletebutton.clicked.connect(
            self.onclickdeletebutton
        ) 
        self.passwordcopy.clicked.connect(
            self.onclickpasswordcopy
        ) 
        self.usernamecopy.clicked.connect(
            self.onclickusernamecopy
        ) 

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "view_service_details"))
        self.addnewservicelabel.setText(_translate("Dialog", "view_service_details"))
        self.savebutton.setText(_translate("Dialog", "Save"))
        self.servicenamelabel.setText(_translate("Dialog", "Service_name(eg. Amazon,Google)"))
        self.usernamelabel.setText(_translate("Dialog", "Username"))
        self.passwordlabel.setText(_translate("Dialog", "Password"))
        self.deletebutton.setText(_translate("Dialog", "Delete"))
        self.usernamecopy.setText(_translate("Dialog", "🔗"))
        self.passwordcopy.setText(_translate("Dialog", "🔗"))
    def listview(self):
        self.MainWindow.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = listviewclass()
        self.ui.listviewwindow(self.window)
        self.window.show()

    def onclicksavebutton(self):
        itsusername=self.usernamelineedit.text()
        itspassword=self.passwordlineedit.text()
        servicename=self.servicenamelineEdit.text()
        command="update  services set itsusername='"+itsusername+"',itspassword='"+itspassword+"',servicename='"+servicename+"' where servicename='"+selected[0]+"' and username='"+username+"';"
        database(command)
        listview(self)
        print(selected)
    def onclickpasswordcopy(self):
        itspassword=self.passwordlineedit.text()
        pyperclip.copy(itspassword)
        print()
    def onclickusernamecopy(self):
        itsusername=self.usernamelineedit.text()
        pyperclip.copy(itsusername)
        print()
    def onclickdeletebutton(self):
        command="delete from  services where servicename='"+selected[0]+"' and username='"+username+"';"
        database(command)
        listview(self)
        print()

class listviewclass(object):
    def listviewwindow(self, listview):
        self.MainWindow = listview

        listview.setObjectName("listview")
        listview.resize(457, 727)
        self.serviceslist = QtWidgets.QListWidget(listview)
        self.serviceslist.setGeometry(QtCore.QRect(0, 70, 451, 591))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 255, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 255, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 255, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.serviceslist.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.serviceslist.setFont(font)
        self.serviceslist.setAutoFillBackground(False)
        self.serviceslist.setStyleSheet("")
        self.serviceslist.setFrameShadow(QtWidgets.QFrame.Raised)
        self.serviceslist.setLineWidth(5)
        self.serviceslist.setProperty("isWrapping", False)
        self.serviceslist.setObjectName("serviceslist")
        self.serviceslist.itemClicked.connect(
            self.onclickserviceslist
        ) 

        # item = QtWidgets.QListWidgetItem()
        # self.serviceslist.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.serviceslist.addItem(item)

        self.addnewservicebutton = QtWidgets.QPushButton(listview)
        self.addnewservicebutton.setGeometry(QtCore.QRect(10, 670, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addnewservicebutton.setFont(font)
        self.addnewservicebutton.setObjectName("addnewservicebutton")
        self.logoutbutton = QtWidgets.QPushButton(listview)
        self.logoutbutton.setGeometry(QtCore.QRect(220, 0, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.logoutbutton.setFont(font)
        self.logoutbutton.setObjectName("logoutbutton")

        self.retranslateUi(listview)
        QtCore.QMetaObject.connectSlotsByName(listview)
        #my stuff
        self.addnewservicebutton.clicked.connect(
            self.onclickaddnewservicebutton
        ) 
        self.logoutbutton.clicked.connect(
            self.onclicklogoutbutton
        ) 

    global show_saved_services

    def show_saved_services(self):
        _translate = QtCore.QCoreApplication.translate
        command="select servicename,itsusername,itspassword from services where username='"+username+"';"
        l=database(command,getoutput=True)
        print(l)
        if len(l)!=0:
            for i in l:
                item = QtWidgets.QListWidgetItem()
                self.serviceslist.addItem(item)
                # item = self.serviceslist.item(i)
                item.setText(_translate("listview", i[0]))

    def retranslateUi(self, listview):
        _translate = QtCore.QCoreApplication.translate
        listview.setWindowTitle(_translate("listview", "Services View"))
        self.serviceslist.setSortingEnabled(True)
        __sortingEnabled = self.serviceslist.isSortingEnabled()
        self.serviceslist.setSortingEnabled(False)
        # item = self.serviceslist.item(0)
        # item.setText(_translate("listview", "amazon prime"))
        # item = self.serviceslist.item(1)
        # item.setText(_translate("listview", "Netflix"))
        self.serviceslist.setSortingEnabled(__sortingEnabled)
        self.addnewservicebutton.setText(_translate("listview", "Add New Service➕🆕"))
        self.logoutbutton.setText(_translate("listview", "Logout👋"))
        #functions running        
        show_saved_services(self)

    def onclicklogoutbutton(self):
        self.MainWindow.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()


    def onclickserviceslist(self,text):
        print(text.text())
        global selected
        command="select servicename,itsusername,itspassword from services where username='"+username+"';"
        l=database(command,getoutput=True)
        print(l)   
        for i in l:
            if i[0]==text.text():
                selected=list(i)
        self.window = QtWidgets.QMainWindow()
        self.ui = edit_viewclass()
        self.ui.edit_viewwindow(self.window)
        self.window.show()
        self.MainWindow.close()
      


                
    global newserviceswindow
    def newserviceswindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = newserviceclass()
        self.ui.newservicewindow(self.window)
        self.window.show()
        self.MainWindow.close()

        self.window = QtWidgets.QMainWindow()
        self.ui = newserviceclass()
        self.ui.newservicewindow(self.window)
        self.window.show()
    def onclickaddnewservicebutton(self):
        newserviceswindow(self)


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

        #getting random passwords
        generated_password = generate_password()
        self.passwordlineedit.setText(generated_password)
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

    def onclicksavebutton(self):
        servicename=self.servicenamelineEdit.text()
        itsusername=self.usernamelineedit.text()
        itspassword=self.passwordlineedit.text()
        command="select * from services;"
        l=database(command,getoutput=True)
        if (servicename,itsusername,itspassword) not in l:
            command="insert into services values('"+username+"','" +servicename+"','"+itsusername+"','"+itspassword+"');"
            database(command)
        self.MainWindow.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = listviewclass()
        self.ui.listviewwindow(self.window)
        self.window.show()

        


        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    app.exec_()
