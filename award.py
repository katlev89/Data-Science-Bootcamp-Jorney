# TASK TO COMPLETE:

# We need to create a program that reads, calculates and displays the total time taken in triathlon during 3 events - 
# swimming, cycling and runnung. The award a participant receives is based on the total time taken to
# complete the triathlon. The qualifying time for awards is 100 minutes.

# Qualifying Criteria: 
# 0 - 100 mins: Within the qualifying time: Provincial Colours;
# 101 - 105 mins: Within 5 minutes of the qualifying time: Provincial Half Colours;
# 106 - 110 mins: Within 10 minutes of the qualifying time: Provincial Scroll;
# 111+ mins: More than 10 minutes off from the qualifying time: No award.

# Defining the variables:
swimming_time = float(input("Please enter swimming time in minutes: "))
cycling_time = float(input("Please enter cycling time in minutes: "))
running_time = float(input("Please enter running time in minutes: "))

# Calculating the total time:
total_time = swimming_time + cycling_time + running_time

# Printing the total time:
print("Total time is: ", total_time)

# Defining the conditions and printing out the outcome:
if total_time <= 100:
    print("Congratulations! You won the Provincial Colours Award!")
    
elif (total_time >= 101) and (total_time <=105):
    print("Congratulation! You won the Provincial Half Colours Award!")
    
elif (total_time >= 106) and (total_time <=110):
    print("Congratulation! You won the Provincial Scroll Award!")
    
elif (total_time >= 111):
    print("Sorry, no award today.")
    
else:
    print("Sorry, no award today.")