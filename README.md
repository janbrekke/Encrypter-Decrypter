# Encrypter-Decrypter
Python Script to encrypt and decrypt text strings based on a secret user determined key

### Prerequisites

You will need some modules to make this work..
These are defined in the "requirements.txt" file.

```
* cryptography
```
### Installing

To install the Prerequisites, simply run the following command:

```
pip install -r requirements.txt
```
### Usage
Shouldn't be to hard..
First download the ZIP, or clone the repository using:

```
git clone https://github.com/janbrekke/Encrypter-Decrypter.git
```
Then start the python file:

```
python encrypt-decrypt.py
```
Before you can start to encrypt you need to create a KEY file. Select menu item 8.
It will ask you for a secret keyword, type it in and hit ENTER.
Now, do NOT forget this keyword!!
If you encrypt lots of text and forget the keyword or need to re-create the keyfile you will NOT be able to get the encrypted information back without the correct key.

Now that you have the KEY file, you can start to encrypt text.

###  Compatability
Tested on both Windows and Linux (Debian, Ubuntu, Kali, Parrot).
Should work perfectly fine on both platforms as long as you have the Cryptography module installed..
For more information on Cryptography, please visit: https://cryptography.io/