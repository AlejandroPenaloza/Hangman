#THIS IS HANGMAN
print('"Hangman"\nA game where you will try to guess which the hidden word is!')
print('\n')
word = input('Input the word to guess:\n')


while True:
    if word.isalpha():
        break
    else:
        word = input('Wrong input, type a valid word:\n')


number_of_letters = len(word)
word_listed_letters = list(word)
print('\n'*15 + 'This space is given for hiding the word\n')
print('_ '*(number_of_letters - 1) + '_')
letters = [letter for letter in bytearray(range(97, 123)).decode("utf-8")]
letters_left = letters


#Function to check if the letter to use is valid
def isletter():
    letter = input('')
    while True:
        if letter in letters_left:
            break
        else:
            letter = input('Wrong input, type a valid letter:\n')
    return letter


#Function to display the hangman according to the chances remaining
def hangman_display(c):
    if c == 1:
        print('-'*10)
    elif c == 2:
        print('|\n'*10)
        hangman_display(1)
    elif c == 3:
        print('_'*6)
        hangman_display(2)
    elif c == 4:
        print('_'*6)
        print('|      |\n'*3 + '|\n'*7)
    elif c == 5:
        print('_'*6)
        print('|      |\n'*3 + '|      O\n' + '|\n'*6)
    elif c == 6:
        print('_' * 6)
        print('|      |\n' * 3 + '|      O\n' + '|      |' + '|\n' * 5)
    elif c == 7:
        print('_' * 6)
        print('|      |\n' * 3 + '|      O\n' + '|      |\n' + '|     /|\n' + '|\n' * 5)
    elif c == 8:
        print('_' * 6)
        print('|      |\n' * 3 + '|      O\n' + '|      |\n' + '|     /|\\\n' + '|\n' * 5)
    elif c == 9:
        print('_' * 6)
        print('|      |\n' * 3 + '|      O\n' + '|      |\n' + '|     /|\\\n' + '/\n' + '|\n' * 4)
    elif c == 10:
        print('_' * 6)
        print('|      |\n' * 3 + '|      O\n' + '|      |\n' + '|     /|\\\n' + '/\\\n' + '|\n' * 4)


'''count = 0    
if try in word:
    ind = [i for i in range(number_of_letters) if word[i] == try]
    else:
        letters_left.remove(try)
        count += 1
        hangman_display(count)
'''
while True:
    #To check if the input is a valid letter
    while True:
        letter = input('\nInput letter to guess:\n')
        if letter in letters_left:
            break
        else:
            letter = input('Wrong input, type a valid letter:\n')
    if letter in word:
        position = [p for p in range(number_of_letters) if word[p] == letter]
        for times in range(len(position)):
            blanks = position[0]
            print('_ ' * blanks + word[position[0]] + ' ', end='')
            if len(position) > 1:
                blanks = position[1] - position[0] - 1
                position = position[1:]
