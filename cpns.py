import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

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
        self.admin_button.clicked.connect(self.admin_selected)
        self.layout.addWidget(self.admin_button)

        self.user_button = QPushButton("Simple User")
        self.user_button.clicked.connect(self.user_selected)
        self.layout.addWidget(self.user_button)

        self.central_widget.setLayout(self.layout)

    def admin_selected(self):
        # Handle admin user selection
        print("Admin User selected")

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
