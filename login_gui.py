from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
import requests
import sys

class LoginWidget(QWidget):
    def __init__(self):
        self.auth = "CG-TFTmKujK1CwFn4B2KXA4hGPR"
        super(LoginWidget, self).__init__()

        self.setGeometry(0, 0, 600, 450)
        self.setWindowTitle("ddswoosh's Crypto App")
        self.setStyleSheet("background-color: #1f1f2e;")
        self.setWindowIcon(QIcon('.gitignore/bitcoin.png'))

        self.username_text = ""
        self.password_text = ""

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        title_layout = QHBoxLayout()

        login_label = QLabel("Login or Register", self)
        login_label.setAlignment(Qt.AlignCenter)
        login_label.setStyleSheet("font-size: 18px; color: #bb86fc;")
        title_layout.addWidget(login_label)

        layout.addLayout(title_layout)

        input_width = 200

        username_input = QLineEdit(self)
        username_input.setPlaceholderText("Username")
        username_input.setStyleSheet("background-color: #42445a; color: #bb86fc; padding: 10px; border-radius: 5px; text-align: center;")
        username_input.setAlignment(Qt.AlignCenter)
        username_input.setFixedWidth(input_width)
        username_input.textChanged.connect(self.on_username_changed)

        password_input = QLineEdit(self)
        password_input.setPlaceholderText("Password")
        password_input.setEchoMode(QLineEdit.Password)
        password_input.setStyleSheet("background-color: #42445a; color: #bb86fc; padding: 10px; border-radius: 5px; text-align: center;")
        password_input.setAlignment(Qt.AlignCenter)
        password_input.setFixedWidth(input_width)
        password_input.textChanged.connect(self.on_password_changed)

        layout.addSpacing(10)  
        layout.addWidget(username_input, alignment=Qt.AlignCenter)
        layout.addWidget(password_input, alignment=Qt.AlignCenter)
        layout.addStretch(1)

        live_data_layout = QHBoxLayout()

        small_logo_1 = QPixmap(".gitignore/bitcoin.png")
        small_logo_1 = small_logo_1.scaledToWidth(50)
        if f.b[0] > 0:
            mini_logo_1 = QPixmap(".gitignore/up.png")
        else:
            mini_logo_1 = QPixmap(".gitignore/down.png")
        mini_logo_1 = mini_logo_1.scaledToWidth(15)

        small_logo_label_1 = QLabel(self)
        small_logo_label_1.setAlignment(Qt.AlignCenter)
        small_logo_label_1.setPixmap(small_logo_1)

        mini_logo_label_1 = QLabel(self)
        mini_logo_label_1.setAlignment(Qt.AlignCenter)
        mini_logo_label_1.setPixmap(mini_logo_1)

        btc = round(f.b[0], 2)
        percentage_label_1 = QLabel(f"%{btc}", self)
        if f.b[0] > 0:
            percentage_label_1.setStyleSheet("font-size: 13px; color: #007941;")
        else:
            percentage_label_1.setStyleSheet("font-size: 13px; color: #ff3300;")

        small_logo_2 = QPixmap(".gitignore/eth.png")
        small_logo_2 = small_logo_2.scaledToWidth(50)
        if f.b[1] > 0:
            mini_logo_2 = QPixmap(".gitignore/up.png")
        else:
            mini_logo_2 = QPixmap(".gitignore/down.png")
        mini_logo_2 = mini_logo_2.scaledToWidth(15)

        small_logo_label_2 = QLabel(self)
        small_logo_label_2.setAlignment(Qt.AlignCenter)
        small_logo_label_2.setPixmap(small_logo_2)

        mini_logo_label_2 = QLabel(self)
        mini_logo_label_2.setAlignment(Qt.AlignCenter)
        mini_logo_label_2.setPixmap(mini_logo_2)

        eth = round(f.b[1], 2)
        percentage_label_2 = QLabel(f"%{eth}", self)
        if f.b[1] > 0:
            percentage_label_2.setStyleSheet("font-size: 13px; color: #007941;")
        else:
            percentage_label_2.setStyleSheet("font-size: 13px; color: #ff3300;")

        small_logo_3 = QPixmap(".gitignore/cosmos.png")
        small_logo_3 = small_logo_3.scaledToWidth(50)
        if f.b[2] > 0:
            mini_logo_3 = QPixmap(".gitignore/up.png")
        else:
            mini_logo_3 = QPixmap(".gitignore/down.png")
        mini_logo_3 = mini_logo_3.scaledToWidth(15)

        small_logo_label_3 = QLabel(self)
        small_logo_label_3.setAlignment(Qt.AlignCenter)
        small_logo_label_3.setPixmap(small_logo_3)

        mini_logo_label_3 = QLabel(self)
        mini_logo_label_3.setAlignment(Qt.AlignCenter)
        mini_logo_label_3.setPixmap(mini_logo_3)

        atom = round(f.b[2], 2)
        percentage_label_3 = QLabel(f"%{atom}", self)
        if f.b[2] > 0:
            percentage_label_3.setStyleSheet("font-size: 13px; color: #007941;")
        else:
            percentage_label_3.setStyleSheet("font-size: 13px; color: #ff3300;")

        live_data_layout.addWidget(small_logo_label_1)
        live_data_layout.addWidget(mini_logo_label_1)
        live_data_layout.addWidget(percentage_label_1)

        live_data_layout.addWidget(small_logo_label_2)
        live_data_layout.addWidget(mini_logo_label_2)
        live_data_layout.addWidget(percentage_label_2)

        live_data_layout.addWidget(small_logo_label_3)
        live_data_layout.addWidget(mini_logo_label_3)
        live_data_layout.addWidget(percentage_label_3)

        layout.addLayout(live_data_layout)

        login_button = QPushButton("Login", self)
        login_button.setStyleSheet("background-color: #6200ea; color: #ffffff; padding: 10px; border-radius: 5px; font-size: 16px;")

        register_button = QPushButton("Register", self)
        register_button.setStyleSheet("background-color: #003366; color: #ffffff; padding: 10px; border-radius: 5px; font-size: 16px;")

        layout.addSpacing(10)  

        layout.addWidget(login_button)
        layout.addWidget(register_button)

    def on_username_changed(self, text):
        self.username_text = text

    def on_password_changed(self, text):
        self.password_text = text

class FrontPage:
    def introCoins(self):
        self.a = ["bitcoin", "ethereum", "cosmos"]
        self.b = []
        for i in self.a:
            r = requests.get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={i}").json()
            change = r[0]["market_cap_change_percentage_24h"]
            self.b.append(change)

if __name__ == "__main__":
    f = FrontPage()
    f.introCoins()
    app = QApplication(sys.argv)
    lw = LoginWidget()
    lw.show()
    sys.exit(app.exec_())
