counts = 0
total_sum = 0


while True:
    users_input = input("Please enter a whole number or -1 to stop: ")
    if users_input == "-1":
        break

number = float(users_input)
total_sum += number

counts += 1

if counts > 0:
    average = total_sum / counts
    print(f"Average of entered nembers: {average}")
else:
    print("No numbers have been entered")
