# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'encrypter_decrypterUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1090, 672)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.grbEncryptionParameters = QtWidgets.QGroupBox(self.centralwidget)
        self.grbEncryptionParameters.setGeometry(QtCore.QRect(10, 10, 1021, 151))
        self.grbEncryptionParameters.setObjectName("grbEncryptionParameters")
        self.lblSecurityControlByte = QtWidgets.QLabel(self.grbEncryptionParameters)
        self.lblSecurityControlByte.setGeometry(QtCore.QRect(110, 110, 31, 20))
        self.lblSecurityControlByte.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSecurityControlByte.setObjectName("lblSecurityControlByte")
        self.chbLdnHex = QtWidgets.QCheckBox(self.grbEncryptionParameters)
        self.chbLdnHex.setGeometry(QtCore.QRect(960, 70, 81, 20))
        self.chbLdnHex.setObjectName("chbLdnHex")
        self.lblLdn = QtWidgets.QLabel(self.grbEncryptionParameters)
        self.lblLdn.setGeometry(QtCore.QRect(540, 70, 91, 21))
        self.lblLdn.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLdn.setObjectName("lblLdn")
        self.lblAad = QtWidgets.QLabel(self.grbEncryptionParameters)
        self.lblAad.setGeometry(QtCore.QRect(40, 70, 111, 20))
        self.lblAad.setObjectName("lblAad")
        self.txtLdn = QtWidgets.QLineEdit(self.grbEncryptionParameters)
        self.txtLdn.setGeometry(QtCore.QRect(650, 70, 291, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtLdn.setFont(font)
        self.txtLdn.setMaxLength(32)
        self.txtLdn.setAlignment(QtCore.Qt.AlignCenter)
        self.txtLdn.setObjectName("txtLdn")
        self.txtSystemTitle = QtWidgets.QLineEdit(self.grbEncryptionParameters)
        self.txtSystemTitle.setGeometry(QtCore.QRect(650, 30, 291, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtSystemTitle.setFont(font)
        self.txtSystemTitle.setMaxLength(34)
        self.txtSystemTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.txtSystemTitle.setObjectName("txtSystemTitle")
        self.txtKey = QtWidgets.QLineEdit(self.grbEncryptionParameters)
        self.txtKey.setGeometry(QtCore.QRect(170, 30, 291, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtKey.setFont(font)
        self.txtKey.setMaxLength(32)
        self.txtKey.setAlignment(QtCore.Qt.AlignCenter)
        self.txtKey.setObjectName("txtKey")
        self.cmbSecurityHeader = QtWidgets.QComboBox(self.grbEncryptionParameters)
        self.cmbSecurityHeader.setGeometry(QtCore.QRect(170, 110, 291, 22))
        self.cmbSecurityHeader.setObjectName("cmbSecurityHeader")
        self.txtFrameCounter = QtWidgets.QLineEdit(self.grbEncryptionParameters)
        self.txtFrameCounter.setGeometry(QtCore.QRect(650, 110, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtFrameCounter.setFont(font)
        self.txtFrameCounter.setMaxLength(8)
        self.txtFrameCounter.setAlignment(QtCore.Qt.AlignCenter)
        self.txtFrameCounter.setObjectName("txtFrameCounter")
        self.lblFrameCounter = QtWidgets.QLabel(self.grbEncryptionParameters)
        self.lblFrameCounter.setGeometry(QtCore.QRect(490, 100, 151, 31))
        self.lblFrameCounter.setWordWrap(True)
        self.lblFrameCounter.setObjectName("lblFrameCounter")
        self.lblSystemTitle = QtWidgets.QLabel(self.grbEncryptionParameters)
        self.lblSystemTitle.setGeometry(QtCore.QRect(550, 40, 81, 16))
        self.lblSystemTitle.setObjectName("lblSystemTitle")
        self.lblKey = QtWidgets.QLabel(self.grbEncryptionParameters)
        self.lblKey.setGeometry(QtCore.QRect(10, 30, 151, 16))
        self.lblKey.setObjectName("lblKey")
        self.txtAad = QtWidgets.QLineEdit(self.grbEncryptionParameters)
        self.txtAad.setGeometry(QtCore.QRect(170, 70, 291, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtAad.setFont(font)
        self.txtAad.setMaxLength(34)
        self.txtAad.setAlignment(QtCore.Qt.AlignCenter)
        self.txtAad.setObjectName("txtAad")
        self.lblClientServer = QtWidgets.QLabel(self.grbEncryptionParameters)
        self.lblClientServer.setGeometry(QtCore.QRect(790, 110, 81, 20))
        self.lblClientServer.setObjectName("lblClientServer")
        self.cmbClientServer = QtWidgets.QComboBox(self.grbEncryptionParameters)
        self.cmbClientServer.setGeometry(QtCore.QRect(880, 110, 121, 22))
        self.cmbClientServer.setObjectName("cmbClientServer")
        self.grbApdu = QtWidgets.QGroupBox(self.centralwidget)
        self.grbApdu.setGeometry(QtCore.QRect(10, 189, 1021, 221))
        self.grbApdu.setObjectName("grbApdu")
        self.textApdu = QtWidgets.QTextEdit(self.grbApdu)
        self.textApdu.setGeometry(QtCore.QRect(10, 30, 1001, 181))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textApdu.setFont(font)
        self.textApdu.setObjectName("textApdu")
        self.grbOutputApdu = QtWidgets.QGroupBox(self.centralwidget)
        self.grbOutputApdu.setGeometry(QtCore.QRect(10, 420, 1021, 191))
        self.grbOutputApdu.setObjectName("grbOutputApdu")
        self.textOutputApdu = QtWidgets.QTextEdit(self.grbOutputApdu)
        self.textOutputApdu.setGeometry(QtCore.QRect(10, 30, 821, 151))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textOutputApdu.setFont(font)
        self.textOutputApdu.setReadOnly(True)
        self.textOutputApdu.setObjectName("textOutputApdu")
        self.btnMakeApdu = QtWidgets.QPushButton(self.grbOutputApdu)
        self.btnMakeApdu.setGeometry(QtCore.QRect(850, 70, 161, 61))
        self.btnMakeApdu.setObjectName("btnMakeApdu")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1090, 26))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.openUserGuide = QtWidgets.QAction(MainWindow)
        self.openUserGuide.setObjectName("openUserGuide")
        self.menuHelp.addAction(self.openUserGuide)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DLMS APDU Encryption/Decryption  Ver - 0.0.6"))
        self.grbEncryptionParameters.setTitle(_translate("MainWindow", "Encryption Parameters"))
        self.lblSecurityControlByte.setText(_translate("MainWindow", "SC"))
        self.chbLdnHex.setText(_translate("MainWindow", "Hex"))
        self.lblLdn.setText(_translate("MainWindow", "LDN (16 Bytes)"))
        self.lblAad.setText(_translate("MainWindow", "Authentication Key"))
        self.lblFrameCounter.setText(_translate("MainWindow", "Frame Counter (4 Bytes)"))
        self.lblSystemTitle.setText(_translate("MainWindow", "System Title"))
        self.lblKey.setText(_translate("MainWindow", "Encryption-Key (16 Bytes)"))
        self.lblClientServer.setText(_translate("MainWindow", "Client/Server"))
        self.grbApdu.setTitle(_translate("MainWindow", "APDU"))
        self.grbOutputApdu.setTitle(_translate("MainWindow", "Result APDU"))
        self.btnMakeApdu.setText(_translate("MainWindow", "Generate APDU"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.openUserGuide.setText(_translate("MainWindow", "User Guide"))
