from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QTabWidget, QStackedWidget, QHBoxLayout, QApplication
from PyQt5.QtGui import QIcon
from login_gui import LoginWidget
import sys

class WalletPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        label = QLabel("Wallet Page")
        label.setStyleSheet("font-size: 20px; color: #bb86fc;")

        layout.addWidget(label, alignment=Qt.AlignCenter)

class CalculatorPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        label = QLabel("Calculator Page")
        label.setStyleSheet("font-size: 20px; color: #bb86fc;")

        layout.addWidget(label, alignment=Qt.AlignCenter)

class MarketPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        label = QLabel("Market Page")
        label.setStyleSheet("font-size: 20px; color: #bb86fc;")

        layout.addWidget(label, alignment=Qt.AlignCenter)

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle("Crypto App")
        self.setStyleSheet("background-color: #1f1f2e;")
        self.setWindowIcon(QIcon('Logos/bitcoin.png'))

        self.tabs = QTabWidget(self)
        self.pages = QStackedWidget(self)

        self.wallet_page = WalletPage()
        self.calculator_page = CalculatorPage()
        self.market_page = MarketPage()

        self.pages.addWidget(self.wallet_page)
        self.pages.addWidget(self.calculator_page)
        self.pages.addWidget(self.market_page)

        self.tabs.addTab(self.wallet_page, "Wallet")
        self.tabs.addTab(self.calculator_page, "Calculator")
        self.tabs.addTab(self.market_page, "Market")

        layout = QHBoxLayout(self)
        layout.addWidget(self.tabs)
        layout.addWidget(self.pages)

if __name__ == "__main__":
    l = LoginWidget.on_login_clicked
    if l == True:
        app = QApplication(sys.argv)
        main_widget = MainWidget()
        main_widget.show()
        sys.exit(app.exec_())
