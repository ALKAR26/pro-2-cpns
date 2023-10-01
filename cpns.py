import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, QDialog, QMessageBox

class AdminLoginDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Admin Login")
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        self.label = QLabel("Admin Login")
        self.layout.addWidget(self.label)

        self.username_label = QLabel("Username:")
        self.layout.addWidget(self.username_label)

        self.username_input = QLineEdit()
        self.layout.addWidget(self.username_input)

        self.password_label = QLabel("Password:")
        self.layout.addWidget(self.password_label)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)
        self.layout.addWidget(self.login_button)

        self.setLayout(self.layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "ALKAR" and password == "12345678":
            # Successful login
            QMessageBox.information(self, "Success", "Admin login successful.")
            self.accept()
        else:
            # Failed login
            QMessageBox.warning(self, "Error", "Invalid username or password.")

class UserSelectionWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("User Selection")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label = QLabel("Please select your user type:")
        self.layout.addWidget(self.label)

        self.admin_button = QPushButton("Admin User")
        self.admin_button.clicked.connect(self.show_admin_login)
        self.layout.addWidget(self.admin_button)

        self.user_button = QPushButton("Simple User")
        self.user_button.clicked.connect(self.user_selected)
        self.layout.addWidget(self.user_button)

        self.central_widget.setLayout(self.layout)

    def show_admin_login(self):
        admin_login_dialog = AdminLoginDialog()
        if admin_login_dialog.exec_() == QDialog.Accepted:
            print("Admin login successful")

    def user_selected(self):
        # Handle simple user selection
        print("Simple User selected")

def main():
    app = QApplication(sys.argv)
    window = UserSelectionWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
