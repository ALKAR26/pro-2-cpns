import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox

# Dictionary to store car data
car_data = {
    "Mumbai": {
        "Sedan": {
            "Maruti Suzuki": {
                "Dzire": 800000,
                "Ciaz": 900000,
                "Baleno": 750000,
                "Swift": 700000,
                "Ertiga": 850000
            },
            "Hyundai": {
                "Verna": 850000,
                "Aura": 820000,
                "i20": 780000,
                "Elantra": 1100000,
                "Accent": 770000
            }
        },
        "SUV": {
            "Hyundai": {
                "Creta": 1100000,
                "Venue": 950000,
                "Tucson": 1500000,
                "Kona": 1400000,
                "Santa Fe": 1800000
            },
            "Kia": {
                "Seltos": 1050000,
                "Sonet": 900000,
                "Sportage": 1200000,
                "Telluride": 1700000,
                "Carnival": 1900000
            }
        }
    },
    # Add more cities and car data as needed...
}

# Dictionary to store user information (username, password, email, and default city)
user_database = {}

class CarPriceLookupApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Car Price Lookup System")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.username_label = QLabel("Username:")
        self.username_entry = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)
        self.email_label = QLabel("Email:")
        self.email_entry = QLineEdit()
        self.sign_up_button = QPushButton("Sign Up")
        self.sign_up_button.clicked.connect(self.sign_up)

        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_entry)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_entry)
        self.layout.addWidget(self.email_label)
        self.layout.addWidget(self.email_entry)
        self.layout.addWidget(self.sign_up_button)

        self.central_widget.setLayout(self.layout)

        self.result_label = QLabel("", self)
        self.result_label.move(50, 250)
        self.result_label.setStyleSheet("color: green")

    def sign_up(self):
        username = self.username_entry.text()
        password = self.password_entry.text()
        email = self.email_entry.text()

        # Check if the username is already taken
        if username in user_database:
            self.result_label.setText("Username already taken. Please choose another username.")
            return

        # Store user information in the database (including email and default city)
        user_database[username] = {
            'password': password,
            'email': email,
            'default_city': "Mumbai"  # Set default city here
        }
        self.result_label.setText("Registration successful!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = CarPriceLookupApp()
    main_window.show()
    sys.exit(app.exec_())

