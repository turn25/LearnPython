from __future__ import print_function
import random
import time
PICS=('''    
    +---+
    |   |
    o   |
        |
        |
        |
=============''','''
    +---+
    |   |
    o   |
    |   |
        |
============''','''
    +---+
    |   |
    o   |
   /|   |
        |
        |
============''','''
    +---+
    |   |
    o   |
   /|\  |
        |
        |
============''','''
    +---+
    |   |
    o   |
   /|\  |
   /    |
        |
============''','''
    +---+
    |   |
    o   |
   /|\  |
   / \  |
        |
============''','''
    +---+
    |   |
   [o   |
   /|\  |
   / \  |
        |
============''','''
    +---+
    |   |
   [o]  |
   /|\  |
   / \  |
        |
============''')
tukhoa='apple banana melon orange pear lemon pineapple'.split()
def randomWord(word):
    wordIndex=random.randint(0,len(word)-1)
    return word[wordIndex]
def displayBoard(PICS,correctLetters,missedLetters,secretWord):
    print(PICS[len(missedLetters)])
    print()
    print('Tu da doan sai: ',end='')
    for letter in missedLetters:
        print(letter,end='')
    print()
    blanks='_'*len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks=blanks[:i]+secretWord[i]+blanks[i+1:]
    for letter in blanks:
        print(letter,end='')
    print()
def getGuess(AlreadyGuessed):
    while True:
        print('Moi ban doan: ')
        guess=raw_input()
        guess=guess.lower()
        if len(guess) != 1 :
            print('Nhap 1 chu cai thoi pls')
        elif guess not in 'qwertyuiopasdfghjklzxcvbnm':
            print('Nhap CHU CAI pls')
        elif guess == AlreadyGuessed:
            print('Chu cai nay ban DA DOAN roi')
        else:
            return guess
def choilai():
    print('Ban co muon choi lai ko ? (co/khong)')
    return raw_input().lower().startswith('c')

print(" H A N G M A N ('-') ")
missedLetters=''
correctLetters=''
secretWord=randomWord(tukhoa)
hetgame=False
while True:
    displayBoard(PICS,correctLetters,missedLetters,secretWord)
    guess=getGuess(correctLetters+missedLetters)
    if guess in secretWord:
        correctLetters=correctLetters+guess
        FoundAllLetters=True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                FoundAllLetters=False
                break
        if FoundAllLetters:
            print('Chuc mung ban da chien thang voi tu khoa la: ',+secretWord)
            hetgame=True
    else:
        missedLetters= missedLetters + guess
    if len(missedLetters) == len(PICS)-1:
        displayBoard(PICS,correctLetters,missedLetters,secretWord)
        print('Ban da thua voi '+str(len(correctLetters))+' cau dung va '+str(len(missedLetters))+' cau sai, tu khoa la: '+secretWord)
        hetgame=True
    if hetgame:
        if choilai():
            missedLetters=''
            correctLetters=''
            secretWord=randomWord(tukhoa)
            hetgame=False
        else:
            break