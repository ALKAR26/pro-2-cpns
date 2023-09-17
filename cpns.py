# Dictionary to store user information
user_database = {}

# Dictionary to store car data
car_data = {
    "Mumbai": {
        "Sedan": {
            "Maruti Suzuki": {
                "Dzire": 800000,
                "Ciaz": 900000
            },
            "Hyundai": {
                "Verna": 850000,
                "Aura": 820000
            }
        },
        "SUV": {
            "Hyundai": {
                "Creta": 1100000,
                "Venue": 950000
            },
            "Kia": {
                "Seltos": 1050000,
                "Sonet": 900000
            }
        }
    },
    "Delhi": {
        "Sedan": {
            "Honda": {
                "City": 900000,
                "Amaze": 800000
            },
            "Maruti Suzuki": {
                "Ciaz": 850000,
                "Baleno": 750000
            }
        },
        "SUV": {
            "Hyundai": {
                "Creta": 1050000,
                "Venue": 900000
            },
            "Mahindra": {
                "XUV300": 950000,
                "Scorpio": 1200000
            }
        }
    },
    "Bangalore": {
        "Sedan": {
            "Toyota": {
                "Corolla": 950000,
                "Yaris": 850000
            },
            "Honda": {
                "City": 920000,
                "Amaze": 820000
            }
        },
        "SUV": {
            "Hyundai": {
                "Creta": 1000000,
                "Venue": 890000
            },
            "Kia": {
                "Seltos": 980000,
                "Sonet": 870000
            }
        }
    }
}

# Function to register a new user
def sign_up():
    print("\nSign-Up Form")
    username = input("Username: ")

    # Check if the username is already taken
    if username in user_database:
        print("Username already taken. Please choose another username.")
        return

    password = input("Password: ")
    confirm_password = input("Confirm Password: ")

    # Check if the passwords match
    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        return

    # Store user information in the database
    user_database[username] = {
        'password': password,
        'city': input("City: "),
        'car_type': None,
        'car_company': None,
        'car_model': None
    }

    print("Registration successful!")

# Function to log in an existing user
def sign_in():
    print("\nSign-In Form")
    username = input("Username: ")
    password = input("Password: ")

    # Check if the username exists in the database
    if username in user_database and user_database[username]['password'] == password:
        print(f"Welcome, {username}!")
        get_car_preferences(username)
    else:
        print("Invalid username or password. Please try again.")

# Function to get user's car preferences
def get_car_preferences(username):
    print("\nCar Preferences")
    user_city = user_database[username]['city']
    print(f"You are in {user_city}.")

    # Get the user's choice of car type
    car_type = input("Enter the type of car you are looking for (Sedan/SUV): ")
    user_database[username]['car_type'] = car_type

    # Get the user's choice of car company
    print(f"Available car companies in {user_city}: {', '.join(car_data[user_city][car_type].keys())}")
    car_company = input("Enter the car company you prefer: ")
    user_database[username]['car_company'] = car_company

    # Get the user's choice of car model
    print(f"Available car models for {car_company} in {user_city}: {', '.join(car_data[user_city][car_type][car_company].keys())}")
    car_model = input("Enter the car model you want: ")
    user_database[username]['car_model'] = car_model
    display_car_price(username)

# Function to display the car price
def display_car_price(username):
    user_city = user_database[username]['city']
    car_type = user_database[username]['car_type']
    car_company = user_database[username]['car_company']
    car_model = user_database[username]['car_model']

    try:
        price = car_data[user_city][car_type][car_company][car_model]
        print(f"The price of {car_model} by {car_company} in {user_city} is ${price}")
    except KeyError:
        print("Invalid car preferences. Please check your input.")

# Main program loop
while True:
    print("\nWelcome to the Car Price Lookup System")
    print("1. Sign In")
    print("2. Sign Up")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        sign_in()
    elif choice == '2':
        sign_up()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
