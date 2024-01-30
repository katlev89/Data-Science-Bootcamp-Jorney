# Initialize variables"
total_sum = 0
count = 0

# Continuous loop to ask for numbers:
while True:
    user_input = input("Please enter a whole number (or -1 to stop): ")
    if user_input == "-1":
        break 
        
    # Converting the total_sum to a float and adding to the total:
    number = float(user_input)
    total_sum += number

    # Counting how many times the numbers have been entered:
    count += 1
    
# Calculating the average and printing out the result:   
if count > 0:
    average = total_sum / count
    print(f"Average of entered numbers: {average}")
else:
    print("No numbers have been entered")