# ================================================
#                  Hangman Game
# ================================================
# Here's a hangman game made by Vincent J. U.
# How it works : the hidden words are saved in variable:words in which is randomly copied from variable:collection.
# user's answer will be saved in variable:s which is a list, variable:i for counting how many mistakes have been 
# done ( as hangman consists of 7 characters so there 7 is the maximum number of attempts allowed ).
# variable:attempt is just a mark for the first user's input, while variable:ulang is a bool will be False 
# if the user's answer matches the hidden word, input's answer will be saved in variable:c

# Feel free to change the codes if there are more efficient way and please let me know!
# Thankyou very much!

import random
collection = ("crocodile","triceratops","llama","dragontail","monster","garlic","dinosaurus","jackfruit","penguin")
words = collection[random.randint(0,len(collection)-1)] #
i=0 
s = list('')
ulang = True
attempt = 1
for j in range (0,len(words)):
    s+="_"
print("".join(s))

while(i<7 and ulang == True):
    c = str(input("Enter a word: "))
    if(c in words):
        for j in range(0,len(words)):
            if(words[j]==c):
                s[j]=c
        answer = "".join(s)
        print(answer)

        if(answer == words):
            print("Yes! You're right!")
            ulang = False
    else:
        i+=1
        print("Wrong! ",7-i,"chance(s) left")
        if(i==7):
            print("Game Over! The answer is [",words,"]")