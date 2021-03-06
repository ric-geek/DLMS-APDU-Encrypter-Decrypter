# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'encrypter_decrypter_ui_new.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1589, 830)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.grb_encryption_parameters = QtWidgets.QGroupBox(self.tab)
        self.grb_encryption_parameters.setObjectName("grb_encryption_parameters")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.grb_encryption_parameters)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_client_server = QtWidgets.QLabel(self.grb_encryption_parameters)
        self.lbl_client_server.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_client_server.setObjectName("lbl_client_server")
        self.gridLayout_2.addWidget(self.lbl_client_server, 3, 0, 1, 1)
        self.lbl_authentication_key = QtWidgets.QLabel(self.grb_encryption_parameters)
        self.lbl_authentication_key.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_authentication_key.setObjectName("lbl_authentication_key")
        self.gridLayout_2.addWidget(self.lbl_authentication_key, 1, 0, 1, 1)
        self.lbl_ldn = QtWidgets.QLabel(self.grb_encryption_parameters)
        self.lbl_ldn.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ldn.setObjectName("lbl_ldn")
        self.gridLayout_2.addWidget(self.lbl_ldn, 1, 3, 1, 1)
        self.lbl_frame_counter = QtWidgets.QLabel(self.grb_encryption_parameters)
        self.lbl_frame_counter.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_frame_counter.setObjectName("lbl_frame_counter")
        self.gridLayout_2.addWidget(self.lbl_frame_counter, 2, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 2, 1, 1)
        self.cmb_security_control_byte = QtWidgets.QComboBox(self.grb_encryption_parameters)
        self.cmb_security_control_byte.setObjectName("cmb_security_control_byte")
        self.gridLayout_2.addWidget(self.cmb_security_control_byte, 2, 1, 1, 1)
        self.txt_system_title = QtWidgets.QLineEdit(self.grb_encryption_parameters)
        self.txt_system_title.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_system_title.setObjectName("txt_system_title")
        self.gridLayout_2.addWidget(self.txt_system_title, 0, 5, 1, 1)
        self.lbl_encryption_key = QtWidgets.QLabel(self.grb_encryption_parameters)
        self.lbl_encryption_key.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_encryption_key.setObjectName("lbl_encryption_key")
        self.gridLayout_2.addWidget(self.lbl_encryption_key, 0, 0, 1, 1)
        self.txt_encryption_key = QtWidgets.QLineEdit(self.grb_encryption_parameters)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_encryption_key.sizePolicy().hasHeightForWidth())
        self.txt_encryption_key.setSizePolicy(sizePolicy)
        self.txt_encryption_key.setMaxLength(32)
        self.txt_encryption_key.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_encryption_key.setObjectName("txt_encryption_key")
        self.gridLayout_2.addWidget(self.txt_encryption_key, 0, 1, 1, 1)
        self.cmb_client_server = QtWidgets.QComboBox(self.grb_encryption_parameters)
        self.cmb_client_server.setObjectName("cmb_client_server")
        self.gridLayout_2.addWidget(self.cmb_client_server, 3, 1, 1, 1)
        self.lbl_system_title = QtWidgets.QLabel(self.grb_encryption_parameters)
        self.lbl_system_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_system_title.setObjectName("lbl_system_title")
        self.gridLayout_2.addWidget(self.lbl_system_title, 0, 3, 1, 2)
        self.lbl_stoc = QtWidgets.QLabel(self.grb_encryption_parameters)
        self.lbl_stoc.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_stoc.setObjectName("lbl_stoc")
        self.gridLayout_2.addWidget(self.lbl_stoc, 3, 3, 1, 1)
        self.txt_frame_counter = QtWidgets.QLineEdit(self.grb_encryption_parameters)
        self.txt_frame_counter.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.txt_frame_counter.setMaxLength(8)
        self.txt_frame_counter.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_frame_counter.setObjectName("txt_frame_counter")
        self.gridLayout_2.addWidget(self.txt_frame_counter, 2, 5, 1, 1)
        self.txt_stoc = QtWidgets.QLineEdit(self.grb_encryption_parameters)
        self.txt_stoc.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_stoc.setObjectName("txt_stoc")
        self.gridLayout_2.addWidget(self.txt_stoc, 3, 5, 1, 1)
        self.lbl_security_control_byte = QtWidgets.QLabel(self.grb_encryption_parameters)
        self.lbl_security_control_byte.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_security_control_byte.setObjectName("lbl_security_control_byte")
        self.gridLayout_2.addWidget(self.lbl_security_control_byte, 2, 0, 1, 1)
        self.btn_encrypt_decrypt = QtWidgets.QPushButton(self.grb_encryption_parameters)
        self.btn_encrypt_decrypt.setMaximumSize(QtCore.QSize(93, 16777215))
        self.btn_encrypt_decrypt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_encrypt_decrypt.setObjectName("btn_encrypt_decrypt")
        self.gridLayout_2.addWidget(self.btn_encrypt_decrypt, 4, 0, 1, 1)
        self.txt_authentication_key = QtWidgets.QLineEdit(self.grb_encryption_parameters)
        self.txt_authentication_key.setMaxLength(32)
        self.txt_authentication_key.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_authentication_key.setObjectName("txt_authentication_key")
        self.gridLayout_2.addWidget(self.txt_authentication_key, 1, 1, 1, 1)
        self.txt_ldn = QtWidgets.QLineEdit(self.grb_encryption_parameters)
        self.txt_ldn.setMaxLength(32)
        self.txt_ldn.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_ldn.setObjectName("txt_ldn")
        self.gridLayout_2.addWidget(self.txt_ldn, 1, 4, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(1, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout_3.addWidget(self.grb_encryption_parameters, 0, 0, 1, 1)
        self.grb_apdu = QtWidgets.QGroupBox(self.tab)
        self.grb_apdu.setObjectName("grb_apdu")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.grb_apdu)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.txt_apdu = QtWidgets.QTextEdit(self.grb_apdu)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txt_apdu.setFont(font)
        self.txt_apdu.setObjectName("txt_apdu")
        self.gridLayout_4.addWidget(self.txt_apdu, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.grb_apdu, 1, 0, 1, 1)
        self.grb_result = QtWidgets.QGroupBox(self.tab)
        self.grb_result.setObjectName("grb_result")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.grb_result)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txt_result = QtWidgets.QTextEdit(self.grb_result)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txt_result.setFont(font)
        self.txt_result.setObjectName("txt_result")
        self.horizontalLayout.addWidget(self.txt_result)
        self.gridLayout_3.addWidget(self.grb_result, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1589, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.grb_encryption_parameters.setTitle(_translate("MainWindow", "Encryption Parameters"))
        self.lbl_client_server.setText(_translate("MainWindow", "Client/Server"))
        self.lbl_authentication_key.setText(_translate("MainWindow", "Authentication Key (16 Bytes)"))
        self.lbl_ldn.setText(_translate("MainWindow", "LDN (16 Bytes)"))
        self.lbl_frame_counter.setText(_translate("MainWindow", "Frame Counter (4 Bytes)"))
        self.lbl_encryption_key.setText(_translate("MainWindow", "Encryption Key (16 Bytes)"))
        self.lbl_system_title.setText(_translate("MainWindow", "System Title"))
        self.lbl_stoc.setText(_translate("MainWindow", "SToC"))
        self.lbl_security_control_byte.setText(_translate("MainWindow", "Security Control Byte (SC)"))
        self.btn_encrypt_decrypt.setText(_translate("MainWindow", "Crypt/Decrypt"))
        self.grb_apdu.setTitle(_translate("MainWindow", "APDU"))
        self.grb_result.setTitle(_translate("MainWindow", "Result"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Encrypter/Decrypter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Converter"))
