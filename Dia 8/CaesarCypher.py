import string

alphabet_string = string.ascii_lowercase
alphabet = list(alphabet_string)

def caesar(text, shift, direction):
    newText = ""
    if direction == 'decode':
            shift *= -1
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            newPosition = position + shift
            if newPosition >= len(alphabet):
                newPosition -= len(alphabet)
            if newPosition < 0:
                newPosition += len(alphabet)
            newLetter = alphabet[newPosition]
            newText += newLetter
        else:
            newText += letter
    print(f'Your {direction}d text is {newText}')


while True:
    while True:
        direction = input('Type encode to encrypt, type decode to decrypt: ')
        if direction == 'encode' or direction == 'decode':
            break
        else:
            print('I dont understand, please try again')
    text_ = input('Type yout message: ').lower()
    shift_ = int(input('Type the shift number: '))

    caesar(text_, shift_, direction)

    again = input('Do you want to use the program again? (yes/no) ').lower()
    if again != 'no' and again != 'yes':
        print('I dont understand, please try again')
    elif again == 'no':
        print('Ok! See you soon')
        break
    
