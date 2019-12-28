import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from encrypter_decrypter_ui import Ui_MainWindow
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from binascii import unhexlify
import sys

USER_GUIDE_FILE = "\\guide\\User_guide.pdf"

def convertLdn(ldn):

    return bytearray.fromhex(ldn).decode() #Converto l'argomento da stringa esadecimale a stringa ASCII

#Funzione che controlla che l'input contenga solo numeri e lettere
def checkInput(stringaInput):

        if (stringaInput.isalnum()):

            return unhexlify(stringaInput)

        if(stringaInput == "-1"):

            return False #Questo if mi serve per evitare di mostrare una doppia MSGbox

        else:

            #Creo la messagebox di errore
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Wrong data!")
            msg.setWindowTitle("Error!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_() #Serve per visualizzare la messagebox

            return False

class mywindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(mywindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnMakeApdu.clicked.connect(self.btnMakeApduClicked)

        self.ui.cmbClientServer.addItem("Client")
        self.ui.cmbClientServer.addItem("Server")

        self.ui.cmbCifraDecifra.addItem("Encrypt")
        self.ui.cmbCifraDecifra.addItem("Decrypt")

        self.ui.cmbCifraDecifra.currentTextChanged.connect(self.lblModificata) #Va messo dopo l'aggiunta delle voci nella combobox altrimenti triggera l'evento

        self.ui.openUserGuide.triggered.connect(self.apriUserGuide)

    def apriUserGuide(self):

        os.startfile(os.getcwd() + USER_GUIDE_FILE)

        return

    def lblModificata(self):

        if(self.ui.cmbCifraDecifra.currentText() == "Decrypt"):

            #Cambio il testo delle label relative alle textbox
            self.ui.lblApdu.setText("Cipher APDU")
            self.ui.lblCipherApdu.setText("APDU")

        else:

            self.ui.lblApdu.setText("APDU")
            self.ui.lblCipherApdu.setText("Cipher APDU")

    def btnMakeApduClicked(self):

        if(self.ui.cmbCifraDecifra.currentText() == "Decrypt"):

            cipherApdu = self.ui.textApdu.toPlainText().replace("\n", "").replace(" ", "") #Rimuovo eventuali newline e spazi

            stringChiperApdu = checkInput(cipherApdu)  # Recupero dalla textbox il dato inserito

            if (stringChiperApdu == False):
                return  #Non proseguo con la decifratura

            stringKey = checkInput(self.ui.txtKey.text())

            if (stringKey == False):
                return

            initVector = checkInput(self.createIV(self.ui.txtFrameCounter.text()))

            if (initVector == False):
                return

            #Inizio a decifrare
            aesgcm = AESGCM(stringKey)

            apdu = aesgcm.encrypt(initVector, stringChiperApdu, unhexlify(self.ui.txtAad.text()))

            apduToString = apdu.hex()

            self.ui.textOutputApdu.setPlainText(apduToString[:-32])

        else:

            apdu = self.ui.textApdu.toPlainText().replace("\n", "").replace(" ", "") #Rimuovo eventuali newline e spazi

            stringApdu = checkInput(apdu)  #Recupero dalla textbox il dato inserito

            if (stringApdu == False):
                return  #Non proseguo con la cifratura

            stringKey = checkInput(self.ui.txtKey.text())

            if (stringKey == False):
                return

            initVector = checkInput(self.createIV(self.ui.txtFrameCounter.text()))

            if (initVector == False):
                return

            #Inizio a cifrare
            aesgcm = AESGCM(stringKey)

            ct = aesgcm.encrypt(initVector, stringApdu, unhexlify(self.ui.txtAad.text()))

            ctToString = ct.hex()

            self.ui.textOutputApdu.setPlainText(ctToString[:-8]) #Il -8 serve per eliminare i 4 byte del TAG di autenticazione che non servono

    #Funzione che si occupa di creare il vettore di inizializzazione
    def createIV(self, frameCounter):

        if(self.ui.cmbClientServer.currentText() == "Client"):

            return self.ui.txtSystemTitle.text() + frameCounter

        else:

            if(self.ui.chbLdnHex.isChecked()):

                if (len(self.ui.txtLdn.text()) != 32):
                    # Creo la messagebox di errore
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("LDN should be express in hex form and 32 character long!")
                    msg.setWindowTitle("Error!")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()  # Serve per visualizzare la messagebox

                    return "-1"  # Ritorno -1 sotto forma di stringa in modo da far fallire la funzione isalnum()

                else:

                    return self.computeServerSystemTitle() + frameCounter

            else:

                if (len(self.ui.txtLdn.text()) != 16):
                    # Creo la messagebox di errore
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("LDN must be 16 character long!")
                    msg.setWindowTitle("Error!")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()  # Serve per visualizzare la messagebox

                    return "-1"  # Ritorno -1 sotto forma di stringa in modo da far fallire la funzione isalnum()

                else:

                    return self.computeServerSystemTitle() + frameCounter

    def computeServerSystemTitle(self):

        charManufId = [] #Creo una lista vuota

        if (self.ui.chbLdnHex.isChecked()):

            charManufId = list(convertLdn(self.ui.txtLdn.text()))

        else:

            charManufId = list(self.ui.txtLdn.text()) #Converto l'LDN inserito in una lista

        # Calcolo un pezzo di system title
        manufacturer_id = ((ord(charManufId[0]) - 64) * 32 * 32) + ((ord(charManufId[1]) - 64) * 32) + (ord(charManufId[2]) - 64)

        startServerSystemTitle = format(manufacturer_id, 'x')  # Mi serve per rimuovere "0x" davanti al valore

        # Formo il Server System Title
        serverSystemTitle = startServerSystemTitle[2:] + startServerSystemTitle[0:2] + charManufId[14] \
                            + charManufId[15] + charManufId[12] + charManufId[13] + charManufId[10] \
                            + charManufId[11] + charManufId[8] + charManufId[9] + charManufId[6] \
                            + charManufId[7] + charManufId[4] + charManufId[5]

        return serverSystemTitle

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
