import requests
from bs4 import BeautifulSoup
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

# Function to scrape car prices
def scrape_car_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the price element based on the website's structure
    price_element = soup.find("span", {"class": "price-class"})  # Replace with the actual HTML structure

    if price_element:
        return price_element.text.strip()
    else:
        return None

# URL of the car listing page
car_url = "https://example.com/car-listing"  # Replace with the URL of the car listing page

# Desired price threshold
desired_price = 20000

# Email address to receive notifications
to_email = "recipient_email@example.com"  # Replace with the recipient's email address

while True:
    current_price = scrape_car_price(car_url)
    
    if current_price:
        current_price = float(current_price.replace("$", "").replace(",", ""))
        
        if current_price <= desired_price:
            subject = "Car Price Alert"
            message = f"The car price is now ${current_price}. It's within your desired price range!"
            send_notification(subject, message, to_email)
            break
    
    # Check the price every 24 hours (86400 seconds)
    time.sleep(86400)
