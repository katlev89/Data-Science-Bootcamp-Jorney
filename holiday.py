# Creating the program to calculate a user’s total holiday cost, 
# which includes the plane cost, hotel cost, and car-rental cost.
print("Welcome to your personalised holiday cost calculator!")

# Getting user's input's:
city_flight = input("Please type in your destination: Sydney, Paris or New York").lower()
num_nights = int(input("Please enter the number of nights you will stay at the hotel: "))
rental_days = int(input("Please enter the number of days you will need a rental car: "))

# Creating 1st function to calculate the hotel cost:

def hotel_cost(num_nights):
    rate_per_night = 100 # Example rate
    return rate_per_night * num_nights

# Creating 2nd function to calculate the flight cost:

def flight_cost(city_flight):
    if city_flight == "sydney":
        return 1500
    elif city_flight == "paris":
        return 200
    elif city_flight == "new york":
        return 750
    else:
        return 0 # The entered city is not listed
    
# Creating 3rd function to calculate the car rental cost:

def rental_car_cost(rental_days):
    rate_per_day = 70 # Example rate
    return rental_days * rate_per_day

# Creating 4th function to calculate the total cost of the holiday:

def total_holiday_cost(num_nights, city_flight, rental_days):
    return hotel_cost(num_nights) + flight_cost(city_flight) + rental_car_cost(rental_days)

# Calculating the total cost
total_cost = total_holiday_cost(num_nights, city_flight, rental_days)

# Printing out all the details in a readable way
print("\nYour Holiday Details:")
print("Destination:", city_flight.title())
print("Number of Nights in Hotel:", num_nights)
print("Hotel Cost: £", hotel_cost(num_nights))
print("Flight to", city_flight.title(), "Cost: £", flight_cost(city_flight))
print("Car Rental for", rental_days, "days Cost: £", rental_car_cost(rental_days))
print("The total cost of your holiday will be: £", total_cost)



