import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QListWidget, QDialog, QInputDialog, QLineEdit, QPushButton, QMessageBox, QListWidgetItem, QAction, QMenu
from PyQt5.QtCore import Qt

class CarPriceSystem(QWidget):
    def __init__(self, car_data):
        super().__init__()

        self.car_data = car_data
        self.current_city = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Car Price System')
        self.setGeometry(500, 250, 500, 400)

        self.car_list = QListWidget(self)
        self.update_car_list()

        self.switch_city_button = QPushButton('Switch City', self)
        self.switch_city_button.clicked.connect(self.switch_city)

        # Add a "Send Notification" button
        self.send_notification_button = QPushButton('Send Notification', self)
        self.send_notification_button.clicked.connect(self.send_notification)

        layout = QVBoxLayout()
        layout.addWidget(self.car_list)
        layout.addWidget(self.switch_city_button)
        layout.addWidget(self.send_notification_button)

        self.setLayout(layout)

    def update_car_list(self):
        self.car_list.clear()

        if self.current_city:
            city_data = self.car_data.get(self.current_city, {})
            for company, models in city_data.items():
                for model, price in models.items():
                    item = QListWidgetItem(f"{self.current_city} - {company} - {model}: ₹{price:.2f}", self.car_list)
                    item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                    item.setCheckState(Qt.Unchecked)

    def switch_city(self):
        city, ok = QInputDialog.getItem(self, 'Switch City', 'Select a city:', list(self.car_data.keys()), 0, False)
        if ok:
            self.current_city = city
            self.update_car_list()

    def send_notification(self):
        # Display a notification message
        QMessageBox.information(self, 'Notification', 'Notification will be sent to your desktop when the sekected car price flicker.')

class LoginPage(QDialog):
    def __init__(self, car_data):
        super().__init__()

        self.car_data = car_data
        self.init_ui()
        self.users = {}

    def init_ui(self):
        self.setWindowTitle('Login Page')
        self.setGeometry(500, 220, 500, 300)

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
            self.accept()
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

if __name__ == '__main__':
    common_car_models = {
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
        'Mahindra': {
            'Thar': 1600000,
            'Bolero': 1200000,
            'Scarpio': 2000000,
            'XUV 300': 8000000,
            'Bolero NEO': 1400000,
        },
         'Hyundai': {
            'Exter': 600000,
            'Creta': 1100000,
            'Grand i10 Nios': 600000,
            'Venue': 800000,
            'Verna': 1200000,
        },
         'Kia': {
            'Seltos': 1500000,
            'Sonet': 800000,
            'Carens':1200000,
            'EV6': 7000000,
        },
        'Tata': {
            'Nexon': 1000000,
            'Harrier': 1500000,
            ' Safari': 1600000,
            'Tata Punch': 800000,
            'Tata Nexon EV': 1800000,
        },
    }

    car_data = {
        'Delhi': common_car_models,
        'Mumbai': common_car_models,
        'Chennai': common_car_models,
        'Kolkata': common_car_models,
        'Dehradun': common_car_models,
        'Patna': common_car_models,
        'Pithoragrah': common_car_models,
        'Chandigrah': common_car_models,
        'Pune': common_car_models,
    }

    app = QApplication(sys.argv)

    login_page = LoginPage(car_data)
    if login_page.exec_() == QDialog.Accepted:
        car_price_system = CarPriceSystem(car_data)
        car_price_system.show()

    sys.exit(app.exec_())
