pyg = 'ay'

import time

original = raw_input('What script would you like to run? ')

if "Pig" or "Latin" or "Pig Latin" or "pig" or "latin" or "pig latin" in original:  
    print "Running script..."
    time.sleep(1)
    question = raw_input("Enter your word: ")
    if len(question) > 0 and question.isalpha(): 
        word = question.lower()
        first = word[0]
        word_uzi = word[1:len(question)]
        new_word = word_uzi + first + pyg
        print new_word 
else:
    print "You didn't type anything"
