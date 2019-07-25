from easygui import*
import sys
import random
score = []
choices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def word_selection():
        global word
        lines = open("list_words.txt").readlines() 
        line = lines[0]
        word_list = line.split()
        word = random.choice(word_list)
def pic(score):
    global picture
    if len(score) == 0:
        picture = "hangman.png"
    elif len(score) == 1:
        picture = "hangman_1.png"
    elif len(score) == 2:
        picture = "hangman_2.png"
    elif len(score) == 3:
        picture = "hangman_3.png" 
    elif len(score) == 4:
        picture = "hangman_4.png"
    elif len(score) == 5:
        picture = "hangman_5.png"
    elif len(score) == 6:
        picture = "hangman_6.png"
    elif len(score) == 7:
        picture = "hangman_7.png"
    elif len(score) == 8:
        picture = "hangman_8.png"
    elif len(score) == 9:
        picture = "hangman_9.png"
    else:
        exit()

word_selection()

wordl = list(word)
print(wordl)

while len(wordl) > 0:
    pic(score)
    image = picture
    msg = "please select a letter"
    reply = buttonbox(msg, image=image, choices=choices)
    choices.remove(reply)
    print(reply)
    try:
        wordl.remove(reply)
        print("correct")
    except ValueError:
        print("wrong letter")
        score.append(1)
        continue
