#########################################
#                                       #
#            Encrypter\Decrypter        #
#                 Software              #
#                                       #
#########################################
# date: 2020/02/18                      #
# name: Jan Brekke                      #
# description: Encrypt and Decrypt text #
# based on a user determined password   #
# created with the key generator.       #
#                                       #
# WARNING!                              #
# DO NOT FORGET the secret password     #
# that you used in the generator!       #
# I am NOT to be held responsible       #
# for any loss you may encouter by      #
# using this python script..            #
# You have been warned!                 #
#########################################

import cryptography, base64, os, os.path
from os import system, name
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def clear(): 
  
    # Windows terminal
    if name == 'nt': 
        _ = system('cls') 
  
    # Linux terminal
    else: 
        _ = system('clear') 

clear()


while True :
    print("\n\n")
    print("*"*56)
    print("\n")
    print("           --DigitalBrekke--")
    print("            EnCrypt/DeCrypt\n")
    print("Choose an option by pressing the corresponging number\n")
    print("       1 :: Encrypt")
    print("       2 :: Decrypt\n")
    print("-"*56)
    print("       8 :: Key Generator")
    print("       9 :: Exit\n")
    print("*"*56)


    # The command that actually ask for a number
    action = input('Option:  ')

    # Encrypter Part
    def encrypter():
        
        if os.path.isfile('crypter.key'):

            file = open('crypter.key', 'rb')
            key = file.read()
            file.close()

            clear()

            message = input("What to Encode?\n")
            messagedata = message.encode()

            f = Fernet(key)
            encrypted = f.encrypt(messagedata)
            encryptedstring = encrypted.decode('ASCII')

            clear()

            print ("\n\n\nYour input Encrypts to:\n"+ encryptedstring)
            print ("\n\n\n")

            input("Press the <ENTER> key to continue...")
            clear()
        
        else:
            clear()
            print("\n\n\nCan't find any encryption keys!\nYou need to generate a KEY first in Menu item 8..\n\n")
            input("Press the <ENTER> key to continue...")
            clear()
            return


    # Decrypter Part
    def decrypter():
        if os.path.isfile('crypter.key'):
            file = open('crypter.key', 'rb')
            key = file.read()
            file.close()

            clear()

            message = input("What to Decode?\n")
            messagedata = message.encode('UTF-8')

            #Test if current key will decode
            try:
                f = Fernet(key)
                decrypted = f.decrypt(messagedata)
                decryptedstring = decrypted.decode('UTF-8')

            except cryptography.fernet.InvalidToken:
                print("\n\n")
                print("-"*40)
                print("\nDecryption Error!!\nUnablble to DeCrypt the input with the secret key stored in crypter.key\nThe current KEY does not match..\n\n")
                input("Press the <ENTER> key to continue...")
                
                clear()
                return

            clear()
            print ("\n\n\nYour input decrypts to:\n"+ decryptedstring)
            print ("\n\n\n")

            input("Press the <ENTER> key to continue...")
            clear()

        else:
            clear()
            print("\n\n\nCan't find any encryption keys!\nYou need to generate a KEY first in Menu item 8..\n\n")
            input("Press the <ENTER> key to continue...")
            clear()
            return
            
    #Generates a Key file
    def keygen():
        clear()
        
        password_provided = input("\n\n\nSet the secret password\nDO NOT FORGET THIS!!\n :: ")
        password = password_provided.encode()
        salt = b'salt_' # Could be changed using a key from os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))

        clear()
        file = open('crypter.key', 'wb')
        file.write(key) # Printing the key to console would show bytes version
        file.close()
        print("Secret Key created!")
        print("Key stored as file: crypter.key\n\n")

        input("Press the <ENTER> key to continue...")
        clear()

    #The options available in the menu at the top
    choice = {'1': encrypter, '2': decrypter, '8': keygen }

    # The exit command since the script is  running in a while loop
    # Yes! I know pressing any other key would also kill it :P
    # but it's nice to have it in there
    if action == '9':
        print("\n\nSee you around!")
        break

    choice[action]()
