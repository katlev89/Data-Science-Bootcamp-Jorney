# This example program is meant to demonstrate errors.
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

### Generally this example has got less errors than the previous one. However I could identify and correct following errors:

### Undefined variable - 'animal = Lion' should be defined as a string. Without quotes, Python won't treat them as such.
### F string syntax - missing the identification of f string
### Logic error in messing up with the variables in the contex of the sentence.
### Print command not executed correctly - syntax error

### It is missing any sort of comments about the program (personal suggest)

animal = "Lion" ### Adding the double quotation marks to correctly assign the variable (runtime error).
animal_type = "cub"  
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth." ### wrong syntaxed f string, 
### messed up with the variable names (syntax, and logic errors).

print(full_spec) ### Missing parentheses and consequentially unnecessary empty space between "print" and "full" - syntax error.

### - My comments
