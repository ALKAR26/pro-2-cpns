import requests
import smtplib
import time

# Function to send an email notification
def send_notification(subject, message, to_email):
    from_email = "your_email@gmail.com"  # Replace with your email
    password = "your_email_password"  # Replace with your email password

    # Create an SMTP server connection
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(from_email, password)

    # Create the email message
    email_message = f"Subject: {subject}\n\n{message}"

    # Send the email
    server.sendmail(from_email, to_email, email_message)

    # Close the server connection
    server.quit()

# Function to fetch car price using the Edmunds API
def fetch_car_price(api_key):
    base_url = "https://api.edmunds.com/api/v2/your_endpoint_here"  # Replace with the actual API endpoint
    parameters = {
        "api_key": api_key,
        # Add any other required parameters here
    }

    response = requests.get(base_url, params=parameters)

    if response.status_code == 200:
        data = response.json()

        # Extract the car price from the API response
        car_price = data["price"]  # Replace with the actual JSON structure

        return car_price
    else:
        return None

# API key from Edmunds (replace with your actual API key)
edmunds_api_key = "your_api_key_here"

# Desired price threshold
desired_price = 20000

# Email address to receive notifications
to_email = "recipient_email@example.com"  # Replace with the recipient's email address

while True:
    current_price = fetch_car_price(edmunds_api_key)
    
    if current_price:
        if current_price <= desired_price:
            subject = "Car Price Alert"
            message = f"The car price is now ${current_price}. It's within your desired price range!"
            send_notification(subject, message, to_email)
            break
    
    # Check the price every 24 hours (86400 seconds)
    time.sleep(86400)
