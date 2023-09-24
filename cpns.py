import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QPushButton, QDialog, QLineEdit, QMessageBox, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class CarPriceSystem(QMainWindow):
    def __init__(self, car_data):
        super().__init__()

        self.car_data = car_data
        self.current_city = None  # Track the currently selected city
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Car Price System')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWebEngineView(self)
        self.setCentralWidget(self.central_widget)
        self.load_home_page()

    def load_home_page(self):
        html = """
        <html>
        <head>
            <title>Car Price System</title>
        </head>
        <body>
            <h1>Select a city:</h1>
            <ul>
                {}
            </ul>
        </body>
        </html>
        """.format("".join([f"<li><a href='car_list/{city}'>{city}</a></li>" for city in self.car_data.keys()]))

        self.central_widget.setHtml(html)

    def load_car_list_page(self, city):
        if city in self.car_data:
            city_data = self.car_data[city]
            html = """
            <html>
            <head>
                <title>Car Price System</title>
            </head>
            <body>
                <h1>{}</h1>
                <ul>
                    {}
                </ul>
                <form method="POST" action="compare">
                    {}
                    <button type="submit">Compare Selected Cars</button>
                </form>
            </body>
            </html>
            """.format(
                city,
                "".join([f"<li><strong>{company}</strong></li><ul>{''.join([f'<li>{model} - ₹{price}</li>' for model, price in models.items()])}</ul>" for company, models in city_data.items()]),
                "".join([f'<input type="checkbox" name="selected_cars" value="{city} - {company} - {model} - ₹{price}">{city} - {company} - {model} - ₹{price}<br>' for company, models in city_data.items() for model, price in models.items()])
            )

            self.central_widget.setHtml(html)

    def load_comparison_page(self, selected_cars):
        html = """
        <html>
        <head>
            <title>Car Price System</title>
        </head>
        <body>
            <h1>Comparison Result</h1>
            <ul>
                {}
            </ul>
        </body>
        </html>
        """.format("".join([f"<li>{car}</li>" for car in selected_cars]))

        self.central_widget.setHtml(html)

class LoginPage(QDialog):
    def __init__(self, car_data):
        super().__init__()

        self.car_data = car_data
        self.init_ui()
        self.users = {'user1': 'password1', 'user2': 'password2'}  # Dictionary to store user credentials

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
        },
        'Honda': {
            'Civic': 2000000,
            'CR-V': 3000000,
            'City': 1000000,
        },
    }

    # Create car data for different cities
    car_data = {
        'Delhi': common_car_models,
        'Mumbai': common_car_models,
    }

    app = QApplication(sys.argv)

    login_page = LoginPage(car_data)
    if login_page.exec_() == QDialog.Accepted:
        car_price_system = CarPriceSystem(car_data)
        car_price_system.show()

    sys.exit(app.exec_())
