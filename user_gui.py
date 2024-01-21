import sys
from main import Get
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QFormLayout, QLabel, QLineEdit, QPushButton, QMenuBar, QAction
from PyQt5.QtGui import QIcon

class Gui(QMainWindow):
    def __init__(self):
        super(Gui, self).__init__()

        self.setWindowTitle("Market Calculator")
        self.setGeometry(100, 100, 800, 600)


        self.setWindowIcon(QIcon('bitcoin_icon.png'))

        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

   
        menubar = self.menuBar()

  
        self.tab_widget = QTabWidget(self.central_widget)
        self.login_register_tab()
        self.crypto_calculator_tab()

    
        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self.tab_widget)

       
        self.create_menu()

    def login_register_tab(self):
        tab = QWidget()
        layout = QFormLayout(tab)

        username_label = QLabel("Username:")
        username_input = QLineEdit()

        password_label = QLabel("Password:")
        password_input = QLineEdit()
        password_input.setEchoMode(QLineEdit.Password)

        login_button = QPushButton("Login")
        register_button = QPushButton("Register")

        layout.addRow(username_label, username_input)
        layout.addRow(password_label, password_input)
        layout.addRow(login_button, register_button)

        self.tab_widget.addTab(tab, "Login/Register")

    def crypto_calculator_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        coin1_label = QLabel("Coin 1:")
        coin1_input = QLineEdit()

        coin2_label = QLabel("Coin 2:")
        coin2_input = QLineEdit()

        calculate_button = QPushButton("Calculate")

        layout.addWidget(coin1_label)
        layout.addWidget(coin1_input)
        layout.addWidget(coin2_label)
        layout.addWidget(coin2_input)
        layout.addWidget(calculate_button)

        self.tab_widget.addTab(tab, "Crypto Calculator")

    def create_menu(self):
        menu_widget = QWidget(self.central_widget)
        menu_layout = QVBoxLayout(menu_widget)

        profile_action = QPushButton("Profile")
        calculator_action = QPushButton("Calculator")
        portfolio_action = QPushButton("Portfolio")

        menu_layout.addWidget(profile_action)
        menu_layout.addWidget(calculator_action)
        menu_layout.addWidget(portfolio_action)

        self.central_widget.layout().addWidget(menu_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    market_calculator_app = Gui()
    market_calculator_app.show()
    sys.exit(app.exec_())
