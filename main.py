import random as random
import words as rand_word
import hangman as hangman

guessedWord = []
word = list(random.choice(rand_word.word).upper())

for i in word:
    guessedWord.append("_ ")

print("\t\t------ WELCOME TO HANGMAN WORLD -------\n")
print(hangman.hangman[0])
print("Rules : ")
print('''
   1. You have to guess a letter so as to complete the blank space
   2. Given that your guessed letter is not in the list, you lose a chance
   3. You have been given 6 lives to save the man from being hanged\n
''')

i = 1
flag = False

while(i < 7) :
    if guessedWord == word:
        print("You won ....\n")
        flag = True
        break

    print("Your word : " + ''.join(guessedWord))
    yourInput = input("Enter a letter to guess : ").upper()

    for k in range(len(word)):
        if yourInput == word[k]:
            guessedWord[k] = yourInput
            flag = True    

    if flag:
        print("Good Choice ")
        i -= 1
    else:
        print("Wrong Choice")
        print(hangman[i])
        
    flag = False
    i += 1

if flag == False:
    print("You could not save the man")
    print(hangman[i-1])
    print("\nThe actual word : " + ''.join(word))
else:
    print("The word : " + ''.join(word))