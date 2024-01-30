#Getting a sentence from the user and storing it as a string:
str_manip = input("Please write a sentence: ")

#Calculation and displaying the length of str_manip:
print(len(str_manip))

#Finding the last letter in str_manip sentence and replacing every its occurence in the sentence with '@':
last_letter = str_manip[-1]

#Replacing every occurence of this letter in the sentence with '@':
modified_str_manip = str_manip.replace(last_letter, "@")

#Displaying the initial and modified sentence:
print("Original sentence: ", str_manip)
print("Modified sentence: ", modified_str_manip)

#Finding the last 3 characters in str_manip and reverse them backwards:
last_three_characters = str_manip[:-4:-1]

#Printing the last 3 characters:
print(last_three_characters)

#Finding the first 3 characters in str_manip:
first_three_characters = str_manip[:3]

#Finding the last 2 characters in str_manip:
last_two_characters = str_manip[-2:]

#Create a five-letter word made up of the first 3 characters and the 2 last characters in str_manip:
print("Five letter word: ", first_three_characters + last_two_characters)