import requests
from bs4 import BeautifulSoup
import smtplib
import time

# Function to scrape car prices from a website
def scrape_car_prices():
    url = 'https://example.com/cars'  # Replace with the URL of the car listings page you want to scrape
    headers = {'User-Agent': 'Your User Agent'}  # Replace with your user agent

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract car prices from the website
    car_prices = []
    car_elements = soup.find_all('div', class_='car-listing')  # Adjust the class name accordingly

    for car in car_elements:
        price = car.find('span', class_='price').text  # Adjust the HTML structure
        car_prices.append(price)

    return car_prices

# Function to send email notifications
def send_email(subject, message):
    sender_email = 'your_email@gmail.com'
    sender_password = 'your_password'
    receiver_email = 'receiver_email@gmail.com'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    email_body = f'Subject: {subject}\n\n{message}'
    server.sendmail(sender_email, receiver_email, email_body)

    server.quit()

# Main loop to check car prices and send notifications
while True:
    car_prices = scrape_car_prices()

    # Check if any car prices meet your criteria
    for price in car_prices:
        if int(price.replace('$', '').replace(',', '')) < 20000:  # Adjust your price threshold
            subject = 'Car Price Alert!'
            message = f'The price of a car is below $20,000: {price}'  # Customize the message
            send_email(subject, message)

    # Check again in 24 hours (adjust the time interval as needed)
    time.sleep(86400)
