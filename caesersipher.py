from caesersipher_ascii import *
should_print = True
while should_print == True:
    print(ascii_art)
    alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    type = int(input("Enter 1 to Encrypt and 2 to Decrypt : "))

    code = input("Enter the code  : ").lower()

    shift = (int(input("Enter the shift at which you want to encrypt or decrypt : ")))%26


    def encryption(c,s):
    
        for letter in c:
            if letter in alphabet:
                letter = alphabet[alphabet.index(letter)+s]
                print(letter ,end="")
            else:
                print(letter,end="")
            
            
    def decryption(c,s):
    
        for letter in c:
            if letter in alphabet:
                letter = alphabet[alphabet.index(letter)-s]
                print(letter ,end="")
            else:
                print(letter,end="")
    
    def selection(t):
        if t == 1 :
        
            print(f"Your Encrypted Code is : ")
            encryption(code,shift)
        elif t == 2 :
        
            print("Your Decrypted code is : ")
            decryption(code,shift)
        else:
            print("!!!You selected wrong option!!!")
            print("Try Again")

    selection(type)

    start_again = input("\n\n\nType yes to continue or No to stop Encoding Decoding ").lower()
    if start_again == "no":
        should_print = False
        print("Good bye")  
        print("Thanks for using")
    
    
    
    

