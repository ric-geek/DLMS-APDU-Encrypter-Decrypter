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
os.chdir('..')
os.rename(str("executable_file\dist\mainLogic"), os.getcwd() + str("executable_file\dist\encrypt_decrypt_dlms_apdu"))
os.rename(str("executable_file\dist\encrypt_decrypt_dlms_apdu\mainLogic.exe"), \
          str("executable_file\dist\encrypt_decrypt_dlms_apdu\encrypt_decrypt_dlms_apdu.exe"))

directory = str("executable_file\dist\encrypt_decrypt_dlms_apdu")

file_da_zippare = get_all_file_paths(directory)

# Create Zip file
with ZipFile('encrypt_decrypt_dlms_apdu.zip','w') as zip:

    for file in file_da_zippare:

        zip.write(file)

# Move the zip file to the correct folder
shutil.move(str("executable_file\encrypt_decrypt_dlms_apdu.zip"), str("executable_file\windows_version"))

# Now remove all unnecessary files
os.remove(str("executable_file\encrypter_decrypter_ui.py"))
os.remove(str("executable_file\mainLogic.py"))
os.remove(str("executable_file\mainLogic.spec"))
os.remove(str("executable_file\encrypter_decrypterUi.ui"))
shutil.rmtree(str("executable_file\dist"), ignore_errors=True)