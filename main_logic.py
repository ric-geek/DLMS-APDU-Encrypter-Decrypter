import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from encrypter_decrypter_ui_new import Ui_MainWindow
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from binascii import unhexlify
import sys

USER_GUIDE_FILE = "\\guide\\User_guide.pdf"
security_control_byte = ["30", "10"]


def convert_ldn(ldn):

    # Converto l'argomento da stringa esadecimale a stringa ASCII
    return bytearray.fromhex(ldn).decode()


# Check if i have HEX string
def check_input(stringa_input):

        if stringa_input.isalnum():

            return unhexlify(stringa_input)

        if stringa_input == "-1":

            return False  # Questo if mi serve per evitare di mostrare una doppia MSGbox

        else:

            # Creo la messagebox di errore
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

        self.ui.btn_encrypt_decrypt.clicked.connect(self.btn_encrypt_decrypt_clicked)

        self.ui.cmb_client_server.addItem("Client")
        self.ui.cmb_client_server.addItem("Server")

        self.ui.cmb_security_control_byte.addItem("30 - Encrypted and Authenticated")
        self.ui.cmb_security_control_byte.addItem("10 - Authenticated")

        # self.ui.openUserGuide.triggered.connect(self.apri_user_guide)

    def apri_user_guide(self):

        os.startfile(os.getcwd() + USER_GUIDE_FILE)

        return

    def lbl_modificata(self):

        if self.ui.cmbCifraDecifra.currentText() == "Decrypt":

            # Cambio il testo delle label relative alle textbox
            self.ui.lblApdu.setText("Cipher APDU")
            self.ui.lblCipherApdu.setText("APDU")

        else:

            self.ui.lblApdu.setText("APDU")
            self.ui.lblCipherApdu.setText("Cipher APDU")

    def btn_encrypt_decrypt_clicked(self):

        if self.ui.cmb_security_control_byte.currentText() == "30 - Encrypted and Authenticated":

            cipher_apdu = self.ui.txt_apdu.toPlainText().replace("\n", "").replace(" ", "")  # Remove newline and space

            string_chiper_apdu = check_input(cipher_apdu)

            if string_chiper_apdu == False:
                return  #Non proseguo con la decifratura

            encryption_key = check_input(self.ui.txt_encryption_key.text())

            if encryption_key == False:

                return

            authentication_key = check_input(self.ui.txt_authentication_key.text())

            if authentication_key == False:

                return

            # Create the AAD
            aad = security_control_byte[0] + authentication_key

            # Create init vector
            init_vector = check_input(self.createIV(self.ui.txt_frame_counter.text()))

            if init_vector == False:
                return

            # Encrypt or Decrypt
            aesgcm = AESGCM(encryption_key)
            apdu = aesgcm.encrypt(init_vector, string_chiper_apdu, unhexlify(aad))
            apdu_to_string = apdu.hex()
            self.ui.txt_result.setPlainText(apdu_to_string[:-8])

        else:

            print("not implemented yet!")

            #Inizio a cifrare
            # aesgcm = AESGCM(stringKey)

            # ct = aesgcm.encrypt(initVector, stringApdu, unhexlify(self.ui.txtAad.text()))

            # ctToString = ct.hex()

            # self.ui.textOutputApdu.setPlainText(ctToString[:-32]) #Il -8 serve per eliminare i 4 byte del TAG di autenticazione che non servono

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

            charManufId = list(convert_ldn(self.ui.txtLdn.text()))

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
