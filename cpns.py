import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QDialog, QInputDialog, QListWidget

class CarPriceSystem(QWidget):
    def __init__(self, cars):
        super().__init__()

        self.cars = cars
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Car Price System')
        self.setGeometry(100, 100, 400, 300)

        self.car_list = QListWidget(self)
        for car, price in self.cars.items():
            self.car_list.addItem(f"{car}: ${price:.2f}")

        layout = QVBoxLayout()
        layout.addWidget(self.car_list)

        self.setLayout(layout)

class LoginPage(QDialog):
    def __init__(self, cars):
        super().__init__()

        self.cars = cars
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
    cars = {
        'Car Model 1': 25000.00,
        'Car Model 2': 32000.00,
        'Car Model 3': 28000.00,
        'Car Model 4': 35000.00,
    }

    app = QApplication(sys.argv)

    login_page = LoginPage(cars)
    if login_page.exec_() == QDialog.Accepted:
        car_price_system = CarPriceSystem(cars)
        car_price_system.show()

    sys.exit(app.exec_())
