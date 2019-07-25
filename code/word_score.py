word = "super"
wordl = list(word)
print(wordl)
while len(wordl) > 0:
    choice = input("what letter")
    try:
        wordl.remove(choice)
    except ValueError:  
        continue 

    
