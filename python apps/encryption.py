alphabet = "abcdefghijklmnopqrstuvwxyz"
newMessage = ""
message = input("Please enter a message: ")
key = int(input("Tell me a numbeer -26 to 26: "))
for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        position = (position + key) % 26
        newMessage += alphabet[position]
    else:
        newMessage += character
print("Your new message is " + newMessage)
