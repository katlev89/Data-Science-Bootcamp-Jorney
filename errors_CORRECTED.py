# This example program is meant to demonstrate errors.
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

### There are quite some errors in this program of all 3 types:
### Syntax errors - for ex. combinations of single&double quotes, missing parentheses.
### Runtime errors - concatenation of different types of variables, wrong way of assignment the variables, indentation errors,
### incorrect use of equality operator ('==').
### Logical error - didn't taking in account the extra 6 months, incorrect use equality operator ('==').

print("Welcome to the error program!") ### Adding the parentheses and deleting the empty spaces (syntax error).
print("") ### Adding the parentheses and deleting the empty space (syntax error). Deleting the indentation (runtime error).
### Printing put an empty line for better program desing by changing from '\n' to "" (not an error, personal suggest).

### Defining all the variables at the beginning of the code and all together makes the readability easier: (personal suggest)

age = 24 ### Modifying the variable name (runtime/logical error). Deleting the indentation, changing the operator ('==') to ('='), 
### deleting "" for correcting assignment - (runtime errors). Merging this line with the next one to simplify the code (no need of it)

# Variable declaring additional years:
years_from_now = 3 ### Deleting the indentation (runtime error).
### Deleting the quotation mark as no need of them for the definition of the numerical variable (runtime error).

# Variable declaring the total of years:
total_years = age + years_from_now

# Variable to calculate the total amount of months from the total amount of years:
total_months = total_years * 12 ### Correcting the name of the saved variable from 'total' to 'total_years' (runtime error).

# Printing out the age:
print(f"I'm  {age} years old.") ### The concatenation as it was before, would not be working in this case as we have different types of variables. 
### The easier and faster way to write this line of code is by using the f string (runtime and syntax errors as missing the parentheses).

# Printing out the total number of years:
print(f"The total number of years: {years_from_now}") ### Usage of f string again.
### Adding the parentheses and correcting the variable name (runtime and syntax errors as missing the parentheses).
### By the way I would not print out this line in the program as its pretty useless - it would have been sufficient the next printed line:

# Printing out the the age in 3 years in 6 months:
print(f"In 3 years and 6 months, I'll be {total_months + 6} months old.") 
### Using the f string again. Adding the parentheses. Adding the 6 months to the total (runtime, syntax and logical errors).

#HINT, 330 months is the correct answer

### - Comments written by me.

