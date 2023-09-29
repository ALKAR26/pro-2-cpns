import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QListWidget, QDialog, QInputDialog, QLineEdit, QPushButton, QMessageBox, QListWidgetItem
from PyQt5.QtCore import Qt  # Import Qt module from PyQt5

class CarPriceSystem(QWidget):
    def __init__(self, car_data):
        super().__init__()

        self.car_data = car_data
        self.current_city = None  # Track the currently selected city
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Car Price System')
        self.setGeometry(100, 100, 400, 300)

        self.car_list = QListWidget(self)
        self.update_car_list()  # Display car data for the initial city

        self.switch_city_button = QPushButton('Switch City', self)
        self.switch_city_button.clicked.connect(self.switch_city)

        self.compare_button = QPushButton('Compare', self)
        self.compare_button.setEnabled(False)  # Disable the Compare button initially
        self.compare_button.clicked.connect(self.compare_cars)

        layout = QVBoxLayout()
        layout.addWidget(self.car_list)
        layout.addWidget(self.switch_city_button)
        layout.addWidget(self.compare_button)

        self.setLayout(layout)

    def update_car_list(self):
        # Clear the current car list
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

    def compare_cars(self):
        selected_items = [item.text() for item in self.car_list.selectedItems()]

        if selected_items:
            QMessageBox.information(self, 'Compare Cars', '\n'.join(selected_items))
        else:
            QMessageBox.warning(self, 'Compare Cars', 'No cars selected for comparison. Please select some cars.')

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

if __name__ == '__main__':
    # Define a common set of car models for all cities
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
    }

    # Create car data for different cities
    car_data = {
        'Delhi': common_car_models,
        'Mumbai': common_car_models,
        'Chennai': common_car_models,
        'Bangalore': common_car_models,
    }

    app = QApplication(sys.argv)

    login_page = LoginPage(car_data)
    if login_page.exec_() == QDialog.Accepted:
        car_price_system = CarPriceSystem(car_data)
        car_price_system.show()

    sys.exit(app.exec_())

    
