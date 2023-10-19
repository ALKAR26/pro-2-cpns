import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class CarPriceNotifier(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Car Price Notifier')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.car_name_label = QLabel('Car Name:')
        self.car_name_input = QLineEdit()
        layout.addWidget(self.car_name_label)
        layout.addWidget(self.car_name_input)

        self.car_price_label = QLabel('Car Price:')
        self.car_price_input = QLineEdit()
        layout.addWidget(self.car_price_label)
        layout.addWidget(self.car_price_input)

        self.threshold_label = QLabel('Price Threshold:')
        self.threshold_input = QLineEdit()
        layout.addWidget(self.threshold_label)
        layout.addWidget(self.threshold_input)

        self.track_button = QPushButton('Track Price')
        self.track_button.clicked.connect(self.track_price)
        layout.addWidget(self.track_button)

        self.setLayout(layout)

    def track_price(self):
        car_name = self.car_name_input.text()
        car_price = float(self.car_price_input.text())
        threshold = float(self.threshold_input.text())

        if car_price < threshold:
            QMessageBox.information(self, 'Price Alert', f'The price of {car_name} is below your threshold!')
        else:
            QMessageBox.information(self, 'Price Alert', f'The price of {car_name} is not below your threshold.')

def main():
    app = QApplication(sys.argv)
    window = CarPriceNotifier()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
