from PyQt5 import QtCore, QtGui, QtWidgets


class alertclass(object):
    def alertwindow(self, Dialog,alerttext):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 50, 250, 250))
        self.label.setSizeIncrement(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog,alerttext)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog,alerttext):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ALERT"))
        
        self.label.setText(_translate("Dialog", alerttext))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = alertclass()
    ui.alertclass(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
