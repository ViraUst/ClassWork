#Author: Vira Ustymenko
#Date: 23rd January 2026
#Description: use the flowchart as a guide to code up a hangman game, shows letters that are
#correct + pictures

words = ['cat','fight','rain','onomatopoeia','aibohphobia','kingdom', 'malice', 'rhododendron', 'compatible', 'oesophagus','saxophone','thoughtfulness','government','universal',\
         'believe','courage','unanimous','yellow','zinc','zucchini','gullible','blank','homework','beutiful','bioengineering']
#all of the words you can choose -^

initial = '''
  +---+
      |
      |
      |
      |
      |
========='''
pictures = ['''
  +---+
      |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
#made by chrishorton

yesno = '+'#check for if the player wants to play again
totalCorrect = 0 #correct words guessed counter
totalwords = 0 #total words guessed counter

while yesno =='+':
    currentPic = pictures[0]
    allEntered = ''#check for repeated letters
    
    option = int(input("Enter a NUMBER from 1 to 25: "))-1
    
    diff = input("Choose a difficulty by typing a WORD(hard/medium/easy/very easy): ")
    
    word = words[option]
    iword = []
    picnum = 0 #to choose pictures later on
    y = 0
    
    for i in word: #to create a checking list which will be changed with every correct letter guessed
        iword.append(i)
    guessing = []
    for b in range(len(word)):
        guessing.append('_')
    
    if diff == 'hard': #difficulty selector
        turns = 7                        # |
    elif diff == 'medium':               # |
        turns = 14                       # |
    elif diff == 'easy':                 # |
        turns = 21                       # |
    elif diff == 'very easy':            # |
        turns = 28     #difficulty selector
    
    special = turns/7 #to determine the chunks of turns after which to print a different picture
    end = False #to determine if the loop should be restarted -- used at the end
    
    print("Welcome to hangman. Please save a life guessing correct word.")
    while turns:
        
        dot = str(guessing)
        for o in dot:
            if o in "[],'":
                dot = dot.replace(o,'')
        print('''
Guess the word: ''',dot)
        
        for y in range(8): #determines which picture to print
            if y == int(picnum):
                currentPic = pictures[y]
                
        print(currentPic)
        print("Turns left: ", turns)
        
        letter = input("Enter a character: ")
        
        index = 0
        
        if letter in allEntered: #checks if the letter has already been entered
            print("This letter has already been entered.")
        else:
            for i in word:
                if i == letter:
                    guessing.pop(index) #to replace '_' with the correctly placed letter
                    guessing.insert(index,letter)
                    index +=1
                else:
                    index +=1
             
            picnum+=1/special  #to print the picture corresponding with the amount of turns left
            turns-=1 
        
        allEntered = allEntered + letter   #to check if the letter has already been entered
        
        if guessing == iword:
            dot = str(guessing)
            for o in dot:
                if o in "[],'":
                    dot = dot.replace(o,'') #<- to achieve a cleaner finished look in the output
            print('''
''',dot,'''
''')
            print("Well done! You guessed the word", "'",word,"'", "correctly with", turns, "turns left.")
            totalCorrect+=1
            end = True
        elif turns == 0:
            print(pictures[7])
            print("You've run out of guesses. The word was", "'",word,"'")
            end = True
        if end==True:
            totalwords+=1
            break
        
        
    yesno = input("Would you like to play again?(+/-): ")
print('''
Correctly guessed words:''',totalCorrect,"out of",totalwords)
print('''
Thank you for playing Hangman!''')