from easygui import*
import sys

score = []
score.append(1)

if len(score) == 0:
    
    picture = "hangman.png"
elif len(score) == 1:
    picture = "hangman_1.png"
elif len(score) == 2:
    picture = "hangman_2.png"
    
image = picture
msg = "what letter do you choose"
choices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
reply = buttonbox(msg, image=image, choices=choices)
choices.remove(reply)

