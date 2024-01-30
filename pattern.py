# Given - make a program that prints out the stars increasing up tp 5 in a row 
# and after decreasing to 0.

#n = 5 # Maximum numbers in the middle row

# Creating a for loop in range from 1 to 10:
for i in range(1, 10): 
# Asking the program to print '*' increasing by i until i reaches n:
    if i <= 10:
        print('*' * i)
# Giving the command to keep printing '*' in the remaining range of i (6,10) in decreasing:
    else:
        print('*' * (10 - i))