from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from encrypter_decrypter_ui_new import Ui_MainWindow
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from binascii import unhexlify
import sys
import os
import string

USER_GUIDE_FILE = "\\guide\\User_guide.pdf"
security_control_byte = ["30", "10"]


def convert_ldn(ldn):

    # Convert from hex string to ASCII string
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

    def btn_encrypt_decrypt_clicked(self):

        if self.ui.cmb_security_control_byte.currentText() == "30 - Encrypted and Authenticated":

            cipher_apdu = self.ui.txt_apdu.toPlainText().replace("\n", "").replace(" ", "")  # Remove newline and space

            string_chiper_apdu = check_input(cipher_apdu)

            if string_chiper_apdu == False:

                return  # Exit btn_clicked function

            encryption_key = check_input(self.ui.txt_encryption_key.text())

            if encryption_key == False:

                return

            # Create the AAD
            aad = check_input(security_control_byte[0] + self.ui.txt_authentication_key.text())

            if aad == False:

                return

            # Create init vector
            init_vector = check_input(self.create_iv(self.ui.txt_frame_counter.text()))

            if init_vector == False:
                return

            # Encrypt or Decrypt
            aesgcm = AESGCM(encryption_key)
            apdu = aesgcm.encrypt(init_vector, string_chiper_apdu, aad)
            apdu_to_string = apdu.hex()

            # TAG start from index -32 and end at index -8 (it's long 12 bytes)
            self.ui.txt_result.setPlainText("APDU: " + apdu_to_string[:-32] + "\nTAG: " + apdu_to_string[-32:-8])

        else:

            from cryptography.hazmat.backends import default_backend
            from cryptography.hazmat.primitives.ciphers import algorithms, modes, Cipher
            from cryptography.hazmat.backends.interfaces import CipherBackend
            from cryptography.hazmat.primitives.ciphers import algorithms, base, modes

            # Create the AAD
            aad = check_input(security_control_byte[1] + self.ui.txt_authentication_key.text())

            if aad == False:

                return

            encryption_key = check_input(self.ui.txt_encryption_key.text())

            if encryption_key == False:

                return

            # Create init vector
            init_vector = check_input(self.create_iv(self.ui.txt_frame_counter.text()))

            if init_vector == False:
                return

            cipher = base.Cipher(
                algorithms.AES(encryption_key),
                modes.GCM(init_vector),
                backend=default_backend()
            )

            encryptor = cipher.encryptor()
            encryptor.authenticate_additional_data(aad)
            encryptor.finalize()

            data = encryptor.tag.hex()

            self.ui.txt_result.setPlainText(data[:-8])

    # This function create init vector
    def create_iv(self, frame_counter):

        if self.ui.cmb_client_server.currentText() == "Client":

            return self.ui.txt_system_title.text() + frame_counter

        else:

            if all(c in string.hexdigits for c in self.ui.txt_ldn.text()):

                if len(self.ui.txt_ldn.text()) != 32:

                    # Creo la messagebox di errore
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("LDN should be express in hex form and 32 character long!")
                    msg.setWindowTitle("Error!")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()  # Serve per visualizzare la messagebox

                    return "-1"  # Ritorno -1 sotto forma di stringa in modo da far fallire la funzione isalnum()

                else:

                    return self.compute_server_system_title(True) + frame_counter

            else:

                if len(self.ui.txt_ldn.text()) != 16:

                    # Creo la messagebox di errore
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("LDN must be 16 character long!")
                    msg.setWindowTitle("Error!")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()  # Serve per visualizzare la messagebox

                    return "-1"  # Ritorno -1 sotto forma di stringa in modo da far fallire la funzione isalnum()

                else:

                    return self.compute_server_system_title(False) + frame_counter

    def compute_server_system_title(self, is_hex):

        char_manuf_id = []  # Create an empty list

        # Check if string is hexdecimal
        if is_hex:

            char_manuf_id = list(convert_ldn(self.ui.txt_ldn.text()))

        else:

            char_manuf_id = list(self.ui.txt_ldn.text())

        # Compute Manufactorer ID
        manufacturer_id = ((ord(char_manuf_id[0]) - 64) * 32 * 32) + ((ord(char_manuf_id[1]) - 64) * 32) + \
                          (ord(char_manuf_id[2]) - 64)

        start_server_system_title = format(manufacturer_id, 'x')  # Remove "0x" prefix

        # Create Server System Title
        server_system_title = start_server_system_title[2:] + start_server_system_title[0:2] + char_manuf_id[14] \
                              + char_manuf_id[15] + char_manuf_id[12] + char_manuf_id[13] + char_manuf_id[10] \
                              + char_manuf_id[11] + char_manuf_id[8] + char_manuf_id[9] + char_manuf_id[6] \
                              + char_manuf_id[7] + char_manuf_id[4] + char_manuf_id[5]

        return server_system_title

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
