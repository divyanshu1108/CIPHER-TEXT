import string

print("MY PROJECT IS IN REFERENCE OF SHIFT CIPHER")
print("Plaintext: The original, readable message")
print("Cipher Key: The secret number of shifts")
print("Encryption: Moving letters forward by the key")
print("Ciphertext: The scrambled, unreadable secret code")
print("Decryption: Moving letters backward by the key to unlock it")
print(" ")
print(" ")
print("*LETS TAKE AN EXAMPLE OF --CAT-- WORD *")
print(" ")
print("HERE PLAINTEXT WILL BE CAT ")
print(" ")
print("LETS SAY YOU HAVE SELECTED CIPHER KEY AS 3 ")
print(" ")
print("SO LETTER WILL BE ENCRYPTED AS C (+3) -> F,, A (+3) -> D,, T (+3) -> W ")
print(" ")
print("NOW YOUR CIPHER TXT OR ENCRYPTED MESSAGE WILL BE --FDW-- ")
print(" ")
print("IF YOU WANT THIS WORD TO BE DECRYPTED THEN THE DECRYPTED MESSAGE OR PLAINTEXT WILL BE --CAT-- ")
print(" ")

a = input("if you are convinced then type a: ")

if a == 'a':
    print("hello we are using shift cipher example today how it works")
    print("1 give cipher text and plain text to find cipher key")
    print("2 give cipher key and cipher text to print plain text")
    print("3 give cipher key and plain text to print cipher text")
    
    choice = int(input("enter your choice: "))

    if choice == 1:
        S = input("enter a cipher text: ")
        plain_input = input("enter a plain text: ")

        # Convert uppercase characters to lowercase
        word = ""
        for char in S:
            if 'A' <= char <= 'Z':
                word += chr(ord(char) + 32)
            else:
                word += char
        S = word
        wor = ""
        for char in plain_input:
            if 'A' <= char <= 'Z':
                wor += chr(ord(char) + 32)
            else:
                wor += char
        plain_input = wor
        # Calculate cipher key from the first valid letter pair
        key = None
        min_len = min(len(S), len(plain_input))
        for i in range(min_len):
            if S[i].isalpha() and plain_input[i].isalpha():
                key = (ord(S[i]) - ord(plain_input[i])) % 26
                break

        if key is not None:
            print("Your cipher key is:", key)
        else:
            print("Could not calculate key. Ensure both inputs contain letters.")

    elif choice == 2:
        key = int(input("enter cipher key: "))
        S = input("enter a cipher text: ")

        plain_text = ""
        for char in S:
            if 'A' <= char <= 'Z':
                plain_text += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
            elif 'a' <= char <= 'z':
                plain_text += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
            else:
                plain_text += char

        print("Decrypted plain text:", plain_text)

    elif choice == 3:
        key = int(input("enter cipher key: "))
        plain_input = input("enter a plain text: ")

        cipher_text = ""
        for char in plain_input:
            if 'A' <= char <= 'Z':
                cipher_text += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            elif 'a' <= char <= 'z':
                cipher_text += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            else:
                cipher_text += char

        print("Encrypted cipher text:", cipher_text)

    else:
        print("Invalid choice! Please select 1, 2, or 3.")

else:
    print("fuck off go learn first.")
