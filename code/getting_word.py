
import random
def word_selection():
        global word
        lines = open("list_words.txt").readlines() 
        line = lines[0]
        word_list = line.split()
        word = random.choice(word_list)
word_selection()


