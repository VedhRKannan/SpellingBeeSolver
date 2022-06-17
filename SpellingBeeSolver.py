word_file = open( /Users/ramalingamkannan/PythonStuff/words.txt, r) #replace with your own file path

wordlist = []
for word in word_file:
        wordlist.append(str(word).lower()[:-1])

def solve_spelling_bee(letters_list, center_letter):
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                'u', 'v', 'w', 'x', 'y', 'z']
    
    unacceptable_letters = [l for l in alphabet if l not in letters_list]
    acceptable_words = []
    
    for word in wordlist:
        if center_letter in word:
            if word not in acceptable_words:
                if len(word) > 3:
                    if any(l in unacceptable_letters for l in word) == False:
                        acceptable_words.append(word)
                        
    return acceptable_words



letters_list = ['c', 'x', 'n', 'l', 'i', 'o', 'e']
center_letter = 'c'
solve_spelling_bee(letters_list, center_letter)