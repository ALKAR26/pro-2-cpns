import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QListWidget, QDialog, QInputDialog, QLineEdit, QPushButton, QMessageBox

class CarPriceSystem(QWidget):
    def __init__(self, car_data):
        super().__init__()

        self.car_data = car_data
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Car Price System')
        self.setGeometry(100, 100, 400, 300)

        self.car_list = QListWidget(self)
        for city, companies in self.car_data.items():
            for company, models in companies.items():
                for model, price in models.items():
                    self.car_list.addItem(f"{city} - {company} - {model}: ₹{price:.2f}")

        layout = QVBoxLayout()
        layout.addWidget(self.car_list)

        self.setLayout(layout)

class LoginPage(QDialog):
    def __init__(self, car_data):
        super().__init__()

        self.car_data = car_data
        self.init_ui()
        self.users = {}  # Dictionary to store user credentials

    def init_ui(self):
        self.setWindowTitle('Login Page')
        self.setGeometry(100, 100, 300, 200)

        self.username_label = QLabel('Username:', self)
        self.username_entry = QLineEdit(self)

        self.password_label = QLabel('Password:', self)
        self.password_entry = QLineEdit(self)
        self.password_entry.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton('Login', self)
        self.signup_button = QPushButton('Sign Up', self)
        self.forgot_password_button = QPushButton('Forgot Password', self)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_entry)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_entry)
        layout.addWidget(self.login_button)
        layout.addWidget(self.signup_button)
        layout.addWidget(self.forgot_password_button)

        self.setLayout(layout)

        self.login_button.clicked.connect(self.login)
        self.signup_button.clicked.connect(self.signup)
        self.forgot_password_button.clicked.connect(self.forgot_password)

    def login(self):
        username = self.username_entry.text()
        password = self.password_entry.text()

        if username in self.users and self.users[username] == password:
            self.accept()  # Close the login dialog and open the main application window
        else:
            QMessageBox.critical(self, 'Login', 'Login Failed. Invalid username or password.')

    def signup(self):
        username = self.username_entry.text()
        password = self.password_entry.text()

        if not username or not password:
            QMessageBox.warning(self, 'Sign Up', 'Username and Password are required for sign up.')
            return

        if username in self.users:
            QMessageBox.warning(self, 'Sign Up', 'Username already exists. Please choose another.')
        else:
            self.users[username] = password
            QMessageBox.information(self, 'Sign Up', 'Sign Up Successful!')

    def forgot_password(self):
        username, ok = QInputDialog.getText(self, 'Forgot Password', 'Enter your username:')
        if ok:
            if username in self.users:
                new_password, ok = QInputDialog.getText(self, 'Forgot Password', 'Enter a new password:')
                if ok:
                    self.users[username] = new_password
                    QMessageBox.information(self, 'Forgot Password', 'Password reset successful!')
            else:
                QMessageBox.warning(self, 'Forgot Password', 'Username not found. Please check the username.')

if __name__ == '__main__':
    car_data = {
        'Delhi': {
            'Toyota': {
                'Camry': 3500000,
                'Fortuner': 3500000,
                'Corolla': 2200000,
                'Innova': 2800000,
                'Yaris': 1100000,
            },
            'Honda': {
                'Civic': 2000000,
                'CR-V': 3000000,
                'Amaze': 700000,
                'City': 1000000,
                'BR-V': 1200000,
            },
        },
        'Mumbai': {
            'Maruti Suzuki': {
                'Swift': 700000,
                'Brezza': 900000,
                'Alto': 400000,
                'Wagon R': 500000,
                'Ciaz': 900000,
            },
            'Hyundai': {
                'i20': 800000,
                'Creta': 1000000,
                'Venue': 800000,
                'Verna': 1000000,
                'Tucson': 2500000,
            },
        },
        'Chennai': {
            'Mahindra': {
                'XUV500': 1500000,
                'Scorpio': 1200000,
                'Thar': 1200000,
                'Bolero': 800000,
                'KUV100': 600000,
            },
            'Tata Motors': {
                'Tiago': 550000,
                'Tigor': 650000,
                'Harrier': 1600000,
                'Nexon': 800000,
                'Safari': 2100000,
            },
        },
        'Bangalore': {
            'Kia': {
                'Seltos': 1200000,
                'Sonet': 800000,
                'Carnival': 2500000,
                'Niro': 1300000,
                'Seltos EV': 1600000,
            },
            'Ford': {
                'EcoSport': 900000,
                'Figo': 700000,
                'Endeavour': 3000000,
                'Aspire': 800000,
                'Freestyle': 800000,
            },
        },
    }

    app = QApplication(sys.argv)

    login_page = LoginPage(car_data)
    if login_page.exec_() == QDialog.Accepted:
        car_price_system = CarPriceSystem(car_data)
        car_price_system.show()

    sys.exit(app.exec_())
