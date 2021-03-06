# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clientUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_clientUIMain(object):
    def setupUi(self, clientUIMain):
        clientUIMain.setObjectName("clientUIMain")
        clientUIMain.setWindowModality(QtCore.Qt.WindowModal)
        clientUIMain.resize(846, 698)
        clientUIMain.setMinimumSize(QtCore.QSize(846, 698))
        clientUIMain.setMaximumSize(QtCore.QSize(846, 698))
        clientUIMain.setBaseSize(QtCore.QSize(846, 698))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        clientUIMain.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/app.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        clientUIMain.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(clientUIMain)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBoxLogin = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxLogin.setEnabled(True)
        self.groupBoxLogin.setGeometry(QtCore.QRect(10, 0, 831, 111))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.groupBoxLogin.setFont(font)
        self.groupBoxLogin.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBoxLogin.setFlat(False)
        self.groupBoxLogin.setObjectName("groupBoxLogin")
        self.pushButtonLogin = QtWidgets.QPushButton(self.groupBoxLogin)
        self.pushButtonLogin.setGeometry(QtCore.QRect(570, 70, 251, 31))
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.lineEditHostName = QtWidgets.QLineEdit(self.groupBoxLogin)
        self.lineEditHostName.setGeometry(QtCore.QRect(80, 30, 191, 21))
        self.lineEditHostName.setObjectName("lineEditHostName")
        self.lineEditUsername = QtWidgets.QLineEdit(self.groupBoxLogin)
        self.lineEditUsername.setGeometry(QtCore.QRect(370, 30, 171, 21))
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.lineEditPassword = QtWidgets.QLineEdit(self.groupBoxLogin)
        self.lineEditPassword.setGeometry(QtCore.QRect(640, 30, 181, 21))
        self.lineEditPassword.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEditPassword.setInputMask("")
        self.lineEditPassword.setText("")
        self.lineEditPassword.setMaxLength(32767)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setPlaceholderText("")
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.labelHostName = QtWidgets.QLabel(self.groupBoxLogin)
        self.labelHostName.setGeometry(QtCore.QRect(10, 30, 71, 21))
        self.labelHostName.setTextFormat(QtCore.Qt.PlainText)
        self.labelHostName.setObjectName("labelHostName")
        self.labelUsername = QtWidgets.QLabel(self.groupBoxLogin)
        self.labelUsername.setGeometry(QtCore.QRect(300, 30, 71, 21))
        self.labelUsername.setTextFormat(QtCore.Qt.PlainText)
        self.labelUsername.setObjectName("labelUsername")
        self.labelPassword = QtWidgets.QLabel(self.groupBoxLogin)
        self.labelPassword.setGeometry(QtCore.QRect(570, 30, 71, 21))
        self.labelPassword.setObjectName("labelPassword")
        self.pushButtonLogout = QtWidgets.QPushButton(self.groupBoxLogin)
        self.pushButtonLogout.setEnabled(False)
        self.pushButtonLogout.setGeometry(QtCore.QRect(300, 70, 241, 31))
        self.pushButtonLogout.setObjectName("pushButtonLogout")
        self.labelUsername.raise_()
        self.labelHostName.raise_()
        self.lineEditHostName.raise_()
        self.lineEditUsername.raise_()
        self.labelPassword.raise_()
        self.lineEditPassword.raise_()
        self.pushButtonLogin.raise_()
        self.pushButtonLogout.raise_()
        self.groupBoxFileBrowsers = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxFileBrowsers.setGeometry(QtCore.QRect(10, 120, 831, 601))
        self.groupBoxFileBrowsers.setMaximumSize(QtCore.QSize(846, 698))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.groupBoxFileBrowsers.setFont(font)
        self.groupBoxFileBrowsers.setTitle("")
        self.groupBoxFileBrowsers.setObjectName("groupBoxFileBrowsers")
        self.treeViewClientDirectory = QtWidgets.QTreeView(self.groupBoxFileBrowsers)
        self.treeViewClientDirectory.setGeometry(QtCore.QRect(20, 10, 401, 381))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.treeViewClientDirectory.setFont(font)
        self.treeViewClientDirectory.setObjectName("treeViewClientDirectory")
        self.tableWidgetServerDirectory = QtWidgets.QTableWidget(self.groupBoxFileBrowsers)
        self.tableWidgetServerDirectory.setGeometry(QtCore.QRect(450, 50, 371, 341))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.tableWidgetServerDirectory.setFont(font)
        self.tableWidgetServerDirectory.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetServerDirectory.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidgetServerDirectory.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetServerDirectory.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tableWidgetServerDirectory.setObjectName("tableWidgetServerDirectory")
        self.tableWidgetServerDirectory.setColumnCount(0)
        self.tableWidgetServerDirectory.setRowCount(0)
        self.pushButtonRootDirectory = QtWidgets.QPushButton(self.groupBoxFileBrowsers)
        self.pushButtonRootDirectory.setGeometry(QtCore.QRect(450, 400, 111, 41))
        self.pushButtonRootDirectory.setObjectName("pushButtonRootDirectory")
        self.pushButtonDeleteDirectory = QtWidgets.QPushButton(self.groupBoxFileBrowsers)
        self.pushButtonDeleteDirectory.setGeometry(QtCore.QRect(680, 400, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.pushButtonDeleteDirectory.setFont(font)
        self.pushButtonDeleteDirectory.setObjectName("pushButtonDeleteDirectory")
        self.pushButtonUpload = QtWidgets.QPushButton(self.groupBoxFileBrowsers)
        self.pushButtonUpload.setGeometry(QtCore.QRect(20, 410, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.pushButtonUpload.setFont(font)
        self.pushButtonUpload.setObjectName("pushButtonUpload")
        self.pushButtonDownload = QtWidgets.QPushButton(self.groupBoxFileBrowsers)
        self.pushButtonDownload.setGeometry(QtCore.QRect(450, 450, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.pushButtonDownload.setFont(font)
        self.pushButtonDownload.setObjectName("pushButtonDownload")
        self.pushButtonCreateDirectory = QtWidgets.QPushButton(self.groupBoxFileBrowsers)
        self.pushButtonCreateDirectory.setGeometry(QtCore.QRect(680, 10, 141, 31))
        self.pushButtonCreateDirectory.setObjectName("pushButtonCreateDirectory")
        self.lineEditNewDirectory = QtWidgets.QLineEdit(self.groupBoxFileBrowsers)
        self.lineEditNewDirectory.setGeometry(QtCore.QRect(450, 10, 211, 31))
        self.lineEditNewDirectory.setObjectName("lineEditNewDirectory")
        self.labelStatus = QtWidgets.QLabel(self.groupBoxFileBrowsers)
        self.labelStatus.setGeometry(QtCore.QRect(20, 510, 411, 21))
        self.labelStatus.setText("")
        self.labelStatus.setObjectName("labelStatus")
        self.labelUploadStatus = QtWidgets.QLabel(self.groupBoxFileBrowsers)
        self.labelUploadStatus.setGeometry(QtCore.QRect(20, 460, 241, 21))
        self.labelUploadStatus.setText("")
        self.labelUploadStatus.setObjectName("labelUploadStatus")
        self.labelDownloadStatus = QtWidgets.QLabel(self.groupBoxFileBrowsers)
        self.labelDownloadStatus.setGeometry(QtCore.QRect(450, 500, 211, 21))
        self.labelDownloadStatus.setText("")
        self.labelDownloadStatus.setObjectName("labelDownloadStatus")
        self.progressBarUpload = QtWidgets.QProgressBar(self.groupBoxFileBrowsers)
        self.progressBarUpload.setGeometry(QtCore.QRect(280, 460, 141, 23))
        self.progressBarUpload.setProperty("value", 0)
        self.progressBarUpload.setTextVisible(True)
        self.progressBarUpload.setObjectName("progressBarUpload")
        self.progressBarDownload = QtWidgets.QProgressBar(self.groupBoxFileBrowsers)
        self.progressBarDownload.setGeometry(QtCore.QRect(680, 500, 141, 23))
        self.progressBarDownload.setProperty("value", 0)
        self.progressBarDownload.setObjectName("progressBarDownload")
        self.groupBoxFileBrowsers.raise_()
        self.groupBoxLogin.raise_()
        clientUIMain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(clientUIMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 846, 21))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        clientUIMain.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(clientUIMain)
        self.statusbar.setObjectName("statusbar")
        clientUIMain.setStatusBar(self.statusbar)
        self.action_Exit = QtWidgets.QAction(clientUIMain)
        self.action_Exit.setObjectName("action_Exit")
        self.action_Exit_2 = QtWidgets.QAction(clientUIMain)
        self.action_Exit_2.setObjectName("action_Exit_2")
        self.menu_file.addAction(self.action_Exit_2)
        self.menubar.addAction(self.menu_file.menuAction())

        self.retranslateUi(clientUIMain)
        QtCore.QMetaObject.connectSlotsByName(clientUIMain)

    def retranslateUi(self, clientUIMain):
        _translate = QtCore.QCoreApplication.translate
        clientUIMain.setWindowTitle(_translate("clientUIMain", "GROUP 6 FTP CLIENT"))
        self.groupBoxLogin.setTitle(_translate("clientUIMain", "Login"))
        self.pushButtonLogin.setText(_translate("clientUIMain", "Login"))
        self.lineEditHostName.setText(_translate("clientUIMain", "ELEN4017.ug.eie.wits.ac.za"))
        self.lineEditUsername.setText(_translate("clientUIMain", "group6"))
        self.labelHostName.setText(_translate("clientUIMain", "Hostname:"))
        self.labelUsername.setText(_translate("clientUIMain", "Username:"))
        self.labelPassword.setText(_translate("clientUIMain", "Password:"))
        self.pushButtonLogout.setText(_translate("clientUIMain", "Logout"))
        self.treeViewClientDirectory.setWhatsThis(_translate("clientUIMain", "<html><head/><body><p>help</p><p>my</p><p>self</p></body></html>"))
        self.pushButtonRootDirectory.setText(_translate("clientUIMain", "Root Directory"))
        self.pushButtonDeleteDirectory.setText(_translate("clientUIMain", "Delete"))
        self.pushButtonUpload.setText(_translate("clientUIMain", "Upload"))
        self.pushButtonDownload.setText(_translate("clientUIMain", "Download"))
        self.pushButtonCreateDirectory.setText(_translate("clientUIMain", "New Folder"))
        self.menubar.setWhatsThis(_translate("clientUIMain", "File"))
        self.menu_file.setTitle(_translate("clientUIMain", "&File"))
        self.action_Exit.setText(_translate("clientUIMain", "&Exit"))
        self.action_Exit_2.setText(_translate("clientUIMain", "&Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    clientUIMain = QtWidgets.QMainWindow()
    ui = Ui_clientUIMain()
    ui.setupUi(clientUIMain)
    clientUIMain.show()
    sys.exit(app.exec_())

