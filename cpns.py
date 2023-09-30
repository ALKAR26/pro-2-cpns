import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QMessageBox

class UserTypeSelector(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("User Type Selector")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel(self)
        self.label.setText("Select your user type:")
        self.label.setGeometry(50, 50, 300, 30)

        self.admin_button = QPushButton("Admin", self)
        self.admin_button.setGeometry(50, 100, 100, 40)
        self.admin_button.clicked.connect(self.show_admin_login)

        self.user_button = QPushButton("User", self)
        self.user_button.setGeometry(200, 100, 100, 40)
        self.user_button.clicked.connect(self.user_selected)

        self.admin_login_window = None

    def user_selected(self):
        self.open_message_box("User")

    def open_message_box(self, user_type):
        msg = f"You selected '{user_type}'"
        self.label.setText(msg)

    def show_admin_login(self):
        self.admin_login_window = AdminLoginWindow()
        self.admin_login_window.show()

class AdminLoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Admin Login")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel(self)
        self.label.setText("Admin Login")
        self.label.setGeometry(150, 20, 100, 30)

        self.username_label = QLabel(self)
        self.username_label.setText("Username:")
        self.username_label.setGeometry(50, 70, 80, 30)

        self.password_label = QLabel(self)
        self.password_label.setText("Password:")
        self.password_label.setGeometry(50, 120, 80, 30)

        self.username_input = QLineEdit(self)
        self.username_input.setGeometry(150, 70, 200, 30)

        self.password_input = QLineEdit(self)
        self.password_input.setGeometry(150, 120, 200, 30)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login", self)
        self.login_button.setGeometry(150, 170, 100, 30)
        self.login_button.clicked.connect(self.admin_login)

    def admin_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "ALKAR" and password == "12345678":
            QMessageBox.information(self, "Admin Login", "Login Successful")
        else:
            QMessageBox.warning(self, "Admin Login", "Invalid Username or Password")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserTypeSelector()
    window.show()
    sys.exit(app.exec_())
