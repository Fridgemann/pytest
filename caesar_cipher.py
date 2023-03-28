from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(txt, shiftVal, objective):
    updatedTxt = ""
    if shiftVal > 26:
        shiftVal = shiftVal % 26
    for letter in txt:
        if objective == "encode":
            if letter not in alphabet:
                updatedTxt += letter
            else:
                position = alphabet.index(letter)
                shiftedPosition = position + shiftVal
                if shiftedPosition > alphabet.index("z"):
                    DiffToZ = alphabet.index("z") - alphabet.index(letter)          #found out how many steps it takes to get to z
                    shiftedPosition = -1 + (shiftVal - DiffToZ)                     #changed shiftedPosition's value to make it loop from the start of the list, substracting the amount of times it shifted until it reached z
                    updatedTxt += alphabet[shiftedPosition]                         #added the letter to the updatedTxt string as done in the previous version of the encryption function
                else:
                    updatedTxt += alphabet[shiftedPosition]
        elif objective == "decode":
            if letter not in alphabet:
                updatedTxt += letter
            else:
                position = alphabet.index(letter)
                shiftedPosition = position - shiftVal
                updatedTxt += alphabet[shiftedPosition]

    
    print(f"The {objective}d text is {updatedTxt}")
            
caesar(txt = text, shiftVal = shift, objective = direction)
         
while True:        
    keep_going = input("Would you like to use the program again? Y/N: ").lower()
    if keep_going == "y":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(txt = text, shiftVal = shift, objective = direction)
    
    elif keep_going == "n":
        print("Thanks for using the program!")
        break
        
    
        



