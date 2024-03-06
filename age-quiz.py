# Interactive program about user's age:

# Asking the user to input the age:
age = int(input("Please enter your age: "))

# Creating different answers depending on the user's input:
if age < 13:
    print("You qualify for the kiddie discount.")

elif age > 100:
    print("Sorry, you are dead.")

elif age == 21:
    print("Congrats on your 21st!")    

elif age >= 65:
    print("Enjoy your retirement!")
    
elif age >= 40:
    print("You're over the hill.")

else: 
    print("Age is but a number.")