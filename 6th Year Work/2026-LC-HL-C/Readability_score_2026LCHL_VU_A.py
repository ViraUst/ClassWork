#Question 16
#Author: Vira Ustymenko
#Date: 22nd October, 2026
#Description: Program calculates readability score

#Function to calculate the readability score of text.
def calculate_readability_score(text): 
# Split the text into a list of words 
    words = text.split() 
    print("\nThe list of words in the text is:\n", words) 
# Initialise the word counters 
    word_count = len(words) # Number of words in list 
    short_word_count = 0
    for o in words:
        if len(o)<=2:
            short_word_count += 1
    print("Short Words: ",short_word_count)
    
    complex_word_count = 0
    for n in words:
        vowels_count = 0
        for m in ('a','o','e','i','u'):
            vowels_count = vowels_count + n.count(m)
        if n[-1]=='e':
            vowels_count = vowels_count-1
        if vowels_count>=3:
            complex_word_count+=1
    print("Complex Words: ", complex_word_count)

# Initialise the number of sentences
    sentence_count = 0
    for i in ('.','!'):
        sentence_count = sentence_count + text.count(i) 

# Calculate the readability score 
    score = 0.4*((word_count/sentence_count)+100*((word_count-short_word_count)/word_count))
    score = round(score, 2) # Round the score to 2 d.p. 

    return score 

# Set the text for analysis 
text1 = "Elaborate sentences influence readability in subtle and unpredictable ways." 
text2 = "I do not like green eggs and ham! I do not like them Sam I am!"

# Calculate the score for text1 
score1 = calculate_readability_score(text1)
print("Readability Score 1: ",score1)
score2 = calculate_readability_score(text2)
print("Readability Score 2: ",score2)

if score1 == score2:
    print("\nBoth scores are the same.")
elif score1>score2:
    print("\nThe second text is easier to read.")
else:
    print("\nThe first text is easier to read.")