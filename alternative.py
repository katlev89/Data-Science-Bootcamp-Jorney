# Writing a program that reads in a string and makes each alternate
# character into an upper case character and each other alternate character
# a lower case character:

# Initializing string:
test_str = input("Please type a sentence: ").lower()

# Alternate cases in String:
# Counting the total of characters, creating a for loop with a condition to check either the letter is even or odd
# and save it to the 'result' variable respectively either as a lower or upper character:
result = ""

for idx in range(len(test_str)):
    if not idx % 2:
        result = result + test_str[idx].upper()
    else:
        result = result + test_str[idx].lower()
 
# Printing result:
print("The alternate case string is : " + str(result))


# Making each alternative word lower and upper case:
# first splitting the sentence into separate words and defining a new variable (list).
# The if i % 2 != 0 condition checks if the index i is odd. If it is, the corresponding word is converted to uppercase.
# If the index is even (else), the word is converted to lowercase.

words = test_str.split()
new_words = []

for i in range(len(words)):
    if i % 2 != 0:
       new_words.append(words[i].upper())
    else:
        new_words.append(words[i].lower())
        
# Joining the created list into a one sentence and saving it as a new variable, than printing out the result:
modified_sentence = " ".join(new_words)
print("Modified sentence: ", modified_sentence)
        