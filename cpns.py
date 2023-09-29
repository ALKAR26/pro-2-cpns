import tkinter as tk

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

# Create a Tkinter window
root = tk.Tk()
root.title("Car Price Lookup System")

# Function to register a new user
def sign_up():
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    email = email_entry.get()
    city = city_entry.get()

    # Check if the username is already taken
    if username in user_database:
        result_label.config(text="Username already taken. Please choose another username.")
        return

    # Check if the passwords match
    if password != confirm_password:
        result_label.config(text="Passwords do not match. Please try again.")
        return

    # Store user information in the database
    user_database[username] = {
        'password': password,
        'email': email,
        'city': city,
        'car_type': None,
        'car_company': None,
        'car_model': None
    }

    result_label.config(text="Registration successful!")

# Function to log in an existing user
def sign_in():
    username = username_login_entry.get()
    password = password_login_entry.get()

    # Check if the username exists in the database
    if username in user_database and user_database[username]['password'] == password:
        result_label.config(text=f"Welcome, {username}!")
        get_car_preferences(username)
    else:
        result_label.config(text="Invalid username or password. Please try again.")

# Function to get user's car preferences
def get_car_preferences(username):
    user_city = user_database[username]['city']

    # Get the user's choice of car type
    car_type = car_type_var.get()

    available_car_companies = car_data[user_city][car_type].keys()
    
    # Check if there are available car companies
    if not available_car_companies:
        result_label.config(text=f"No available car companies in {user_city} for {car_type}. Please try another type.")
        return

    # Get the user's choice of car company
    car_company = car_company_var.get()

    available_car_models = car_data[user_city][car_type][car_company].keys()

    # Get the user's choice of car model
    car_model = car_model_var.get()
    
    display_car_price(username, user_city, car_type, car_company, car_model)

# Function to display the car price in rupees
def display_car_price(username, user_city, car_type, car_company, car_model):
    try:
        price = car_data[user_city][car_type][car_company][car_model]
        price_in_rupees = "₹{:,.2f}".format(price)
        result_label.config(text=f"The price of {car_model} by {car_company} in {user_city} is {price_in_rupees}")
    except KeyError:
        result_label.config(text="Invalid car preferences. Please check your input.")

# Create GUI elements
username_label = tk.Label(root, text="Username:")
username_entry = tk.Entry(root)
password_label = tk.Label(root, text="Password:")
password_entry = tk.Entry(root, show="*")
confirm_password_label = tk.Label(root, text="Confirm Password:")
confirm_password_entry = tk.Entry(root, show="*")
email_label = tk.Label(root, text="Email:")
email_entry = tk.Entry(root)
city_label = tk.Label(root, text="City:")
city_entry = tk.Entry(root)
sign_up_button = tk.Button(root, text="Sign Up", command=sign_up)

username_login_label = tk.Label(root, text="Username:")
username_login_entry = tk.Entry(root)
