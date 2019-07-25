
    score = []
    score.append(1)
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
        


