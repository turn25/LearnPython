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
tukhoa={'trai cay':'apple orange lemon lime pear watermelon grape grape fruit cherry banana cantalope mango strawberry tomato'.split(), 'dong vat':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split(),'thuc an':'pizza hamburger noodle'.split(),'hinh dang':'square triangle rectangle circle ellipse rhombus trapazoid chevron pentagon hexagon septagon octogon'.split()}
tukhoa1={'trai cay':'tao nho chuoi'.split(),'dong vat':'cho meo cao'.split()}
def randomWord(word):
    wordKey=random.choice(word.keys())
    wordIndex=random.randint(0,len(word[wordKey])-1)
    print('Day la tu khoa lien quan den '+wordKey)
    #choosenword=word[wordKey][wordIndex]
    return word[wordKey][wordIndex]
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
print()
print('Ban muon choi Hangman voi tu khoa bang Tieng Viet hay Tieng Anh?: (1:Tieng Viet/ 2:Tieng Anh)',end='')
ngonngu=raw_input()
if ngonngu=='1':
    secretWord=randomWord(tukhoa1)
    print('Ban da chon ngon ngu tieng Viet')
elif ngonngu not in '12':
    print('Moi CHON 1 hoac 2:')
elif len(ngonngu) !=1:
    print('NHAP 1 HOAC 2 PLS:')
else: #ngonngu=='2':
    secretWord=randomWord(tukhoa)
    print('Ban da chon ngon ngu tieng ANh')
#secretWord=randomWord(tukhoa)
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
            print('Chuc mung ban da chien thang voi tu khoa la: '+secretWord)
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
            print('Ban muon choi Hangman voi tu khoa bang Tieng Viet hay Tieng Anh?: (1:Tieng Viet/ 2:Tieng Anh)',end='')
            ngonngu=raw_input()
            if ngonngu=='1':
                secretWord=randomWord(tukhoa1)
                print('Ban da chon ngon ngu tieng Viet')
            elif ngonngu not in '12':
                print('Moi CHON 1 hoac 2:')
            elif len(ngonngu) !=1:
                print('NHAP 1 HOAC 2 PLS:')
            else: #ngonngu=='2':
                secretWord=randomWord(tukhoa)
                print('Ban da chon ngon ngu tieng ANh')
            hetgame=False
        else:
            break