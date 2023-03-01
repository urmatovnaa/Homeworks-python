from random import choice

HANGMAN = ("""
------
|    |
|
|
|
|
|
|
|
--------
""", """
------
|    |
|    O  |
|
|
|
|
|
|
--------
""", """
------
|    |
|    O
|   -+-
|
|
|
|
|
--------
""", """
------
|    |
|    O
|  /-+-/
|
|
|
|
|
--------
""", """
------
|    |
|    O
|  /-+-/
|    |
|
|
|
|
--------
""", """
------
|    |
|    O
|  /-+-/
|    |
|    |
|   |
|   |
|
--------
""", """
------
|    |
|    O
|  /-+-/
|    |
|    |
|   | |
|   | |
|
--------
""")

print("\t\t\tДобро пожаловать в игру 'Виселица'!")

print(""" Сейчас я загадаю слово, а вы должны будете по буквам его угадать. 
Вы будете предлагать по одной букве, если эта буква есть в моем слове, то я открою вам ее положение в слове. 
Если же нет, то я буду дорисовывать человечка на виселица. Игра будет длиться до тех пор, 
пока вы не отгадаете слово, либо пока человечек не полностью повешен. 
Итак, осталось, только пожелать вам удачи, ведь от вас зависит судьба, несчастного рисованного человечка! """)

maximum = len(HANGMAN) - 1
words = ['marvel', 'codify', 'mouse']
words = list(map(str.upper, words))
main_word = choice(words)
guess_word = list('_' * len(main_word))
counter = 0
lst = []

while counter < maximum and guess_word != main_word:
    print(HANGMAN[counter])
    guess = input("\n\nВведите букву: ")
    guess = guess.upper()

    while guess in lst:
        print("Вы уже предлагали букву: ", guess)
        guess = input("\n\nВведите букву: ")
        guess = guess.upper()

    lst.append(guess)

    if guess in main_word:
        print("\nДа! Буква", guess, "есть в слове!")
        new = ""
        for i in range(len(main_word)):
            if guess == main_word[i]:
                new += guess
            else:
                new += guess_word[i]
        guess_word = new
    else:
        print("\nК сожалению, буквы", guess, "нет в слове.")
        counter += 1

if counter == maximum:
    print(HANGMAN[counter])
    print("\nЧеловечка повесили!")
else:
    print("\nВы отгадали!")
print("\nБыло загаданно слово", main_word, ".")
input("\n\nНажмите ENTER чтобы выйти из игры.")
