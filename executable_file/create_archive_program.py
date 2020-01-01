import os
import shutil
from zipfile import ZipFile

def get_all_file_paths(directory):

    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):

        for filename in files:

            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths

# Rename program's folder
os.rename(os.getcwd() + str("\dist\mainLogic"), os.getcwd() + str("\dist\encrypt_decrypt_dlms_apdu"))
os.rename(os.getcwd() + str("\dist\encrypt_decrypt_dlms_apdu\mainLogic.exe"), \
          os.getcwd() + str("\dist\encrypt_decrypt_dlms_apdu\encrypt_decrypt_dlms_apdu.exe"))

directory = os.getcwd() + str("\dist\encrypt_decrypt_dlms_apdu")

file_da_zippare = get_all_file_paths(directory)

# Create Zip file
with ZipFile('encrypt_decrypt_dlms_apdu.zip','w') as zip:

    for file in file_da_zippare:

        zip.write(file)

# Move the zip file to the correct folder
shutil.move(os.getcwd() + str("\encrypt_decrypt_dlms_apdu.zip"), os.getcwd() + str("\windows_version"))

# Now remove all unnecessary files
os.remove(os.getcwd() + str("\encrypter_decrypter_ui.py"))
os.remove(os.getcwd() + str("\mainLogic.py"))
os.remove(os.getcwd() + str("\mainLogic.spec"))
os.remove(os.getcwd() + str("\encrypter_decrypterUi.ui"))
shutil.rmtree(os.getcwd() + str("\dist"), ignore_errors=True)