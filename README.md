# Shift Cipher Tool

An interactive Python command-line application that demonstrates the mechanics of a Shift Cipher (Caesar Cipher). The tool allows users to encrypt messages, decrypt messages, or analyze text to discover a hidden encryption key.

## Overview
This project provides a hands-on introduction to fundamental cryptography concepts. It breaks down the process of encoding and decoding text using a mathematical shift key. The program serves as an educational tool, providing interactive definitions, text examples (such as transforming "CAT" into "FDW" using a key of 3), and practical execution modes for cryptographic testing.

## Features
*Interactive Introduction:** Explains core cryptographic terms (Plaintext, Ciphertext, Encryption, Decryption) with step-by-step examples.
* Key Discovery Mode:** Calculates the hidden cipher key by comparing a known plaintext and ciphertext pair.
* Decryption Mode:** Decodes an encrypted ciphertext back into readable plaintext using a specific key.
* Encryption Mode:** Encrypts standard plaintext into secure ciphertext using a user-specified shift key.
* Character Protection:** Preserves spaces, punctuation, and non-alphabetic characters during the transformation process.

## Technologies Used
* Python 3.x** - Core programming language
* Built-in Libraries** - Standard string manipulation tools (`string`)

## Steps to Install & Run the Project

### Prerequisites
Make sure you have Python 3 installed on your system. You can check your version by running:
```bash
python --version
```

### Setup and Execution
1. **Clone the repository** to your local machine:
   ```bash
   git clone https://github.com
   ```
2. **Navigate** into the project directory:
   ```bash
   cd YOUR-REPOSITOR
   ```
3. **Run the program** using your terminal:
   ```bash
   python main.py
   ```
   *(Note: Replace `main.py` with the actual name of your Python file if it is named differently).*

## Instructions for Testing

When you run the script, follow these steps to verify its functionality:

1. **Accept the Introduction:** Type `a` when prompted to agree to the terms and enter the main menu.
2. **Test Key Discovery (Choice 1):** 
   * Enter choice `1`
   * Enter cipher text: `fdw`
   * Enter plain text: `cat`
   * *Expected output:* `Your cipher key is: 3`
3. **Test Decryption (Choice 2):** 
   * Enter choice `2`
   * Enter cipher key: `3`
   * Enter cipher text: `FDW`
   * *Expected output:* `Decrypted plain text: CAT`
4. **Test Encryption (Choice 3):** 
   * Enter choice `3`
   * Enter cipher key: `3`
   * Enter plain text: `CAT`
   * *Expected output:* `Encrypted cipher text: FDW`


NOTE 
I HAD USED UBUNTU TERMINAL 
IF YOU HAD TO RUN THIS CODE IN UBUNTU TERMINAL FOLLOW THE STEP WHICH I HAVE MARKED UPWARD 
THANKYOU
