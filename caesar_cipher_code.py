alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#function called 'encrypt' that takes the 'text' and 'shift_amount' as inputs.
def encrypt(plain_text, shift_amount):
    #Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
    cipher_text = ''
    for i in text:
    	index_value = alphabet.index(i)+shift_amount
    	if index_value > 25:
    		index_value = shift_amount - 1
    	cipher_text += ''.join(alphabet[index_value])
    print(f"The encoded text is {cipher_text}")

#function called 'decrypt' that takes the 'text' and 'shift_amount' as inputs.
def decrypt(plain_text, shift_amount):

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
    cipher_text = ''
    for i in text:
    	index_value = alphabet.index(i)-shift_amount
    	if index_value < 0:
    		index_value = shift_amount +25
    	cipher_text += ''.join(alphabet[index_value])
    print(f"The encoded text is {cipher_text}")


while True:

	if direction == 'encode':
		encrypt(text, shift)
		decision = input("Do you want to continue? Type 'y' for yes and 'n' for no:\n").lower()
		if decision == 'y':
			direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
			text = input("Type your message:\n").lower()
			shift = int(input("Type the shift number:\n"))
			continue 	
		else:
			print("Thanks for using the Encoder..!")
			break
	elif direction == 'decode':
		decrypt(text, shift)
		decision = input("Do you want to continue? Type 'y' for yes and 'n' for no:\n").lower()
		if decision == 'y':
			direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
			text = input("Type your message:\n").lower()
			shift = int(input("Type the shift number:\n"))
			continue 
		else:
			print("Thanks for using the Decoder..!")
			break
	else:
		print("Something went wrong. Please provide right inputs.")
		break



