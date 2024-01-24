from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QApplication, QMessageBox
from PyQt5.QtCore import Qt, QObject
from PyQt5.QtGui import QIcon,QPixmap
from auth import User
import requests
import sys

class LoginWidget(QWidget, QObject):
    def __init__(self):
        self.auth = "CG-TFTmKujK1CwFn4B2KXA4hGPR"
        super().__init__()

        self.setGeometry(0, 0, 600, 450)
        self.setWindowTitle("ddswoosh's Crypto App")
        self.setStyleSheet("background-color: #1f1f2e;")
        self.setWindowIcon(QIcon('Logos/bitcoin.png'))

        self.username_text = ""
        self.password_text = ""

        self.init_ui()

    def popUp(self, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Authentication Error")
        msg_box.setText(message)
        msg_box.exec_()

    def init_ui(self):
        layout = QVBoxLayout(self)

        title_layout = QHBoxLayout()

        login_label = QLabel("Login or Register", self)
        login_label.setAlignment(Qt.AlignCenter)
        login_label.setStyleSheet("font-size: 18px; color: #bb86fc;")
        title_layout.addWidget(login_label)

        layout.addLayout(title_layout)

        input_width = 200

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        self.username_input.setStyleSheet("background-color: #42445a; color: #bb86fc; padding: 10px; border-radius: 5px; text-align: center;")
        self.username_input.setAlignment(Qt.AlignCenter)
        self.username_input.setFixedWidth(input_width)
        self.username_input.textChanged.connect(self.on_username_changed)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("background-color: #42445a; color: #bb86fc; padding: 10px; border-radius: 5px; text-align: center;")
        self.password_input.setAlignment(Qt.AlignCenter)
        self.password_input.setFixedWidth(input_width)
        self.password_input.textChanged.connect(self.on_password_changed)

        layout.addSpacing(10)  
        layout.addWidget(self.username_input, alignment=Qt.AlignCenter)
        layout.addWidget(self.password_input, alignment=Qt.AlignCenter)
        layout.addStretch(1)

        live_data_layout = QHBoxLayout()

        small_logo_1 = QPixmap("Logos/bitcoin.png")
        small_logo_1 = small_logo_1.scaledToWidth(50)
        if f.b[0] > 0:
            mini_logo_1 = QPixmap("Logos/up.png")
        else:
            mini_logo_1 = QPixmap("Logos/down.png")
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

        small_logo_2 = QPixmap("Logos/eth.png")
        small_logo_2 = small_logo_2.scaledToWidth(50)
        if f.b[1] > 0:
            mini_logo_2 = QPixmap("Logos/up.png")
        else:
            mini_logo_2 = QPixmap("Logos/down.png")
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

        small_logo_3 = QPixmap("Logos/cosmos.png")
        small_logo_3 = small_logo_3.scaledToWidth(50)
        if f.b[2] > 0:
            mini_logo_3 = QPixmap("Logos/up.png")
        else:
            mini_logo_3 = QPixmap("Logos/down.png")
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
        login_button.clicked.connect(self.on_login_clicked)
        login_button.installEventFilter(self)

        register_button = QPushButton("Register", self)
        register_button.setStyleSheet("background-color: #003366; color: #ffffff; padding: 10px; border-radius: 5px; font-size: 16px;")
        register_button.clicked.connect(self.on_register_clicked)
        register_button.installEventFilter(self)

        layout.addSpacing(10)  

        layout.addWidget(login_button)
        layout.addWidget(register_button)

    def on_login_clicked(self):
        l = u.login(self.username_text,self.password_text)
        if l == True:
            return True
        
    def on_register_clicked(self):
        l = u.register(self.username_text,self.password_text)
        if l == True:
            return True
        
    def on_username_changed(self, text):
        self.username_text = text

    def on_password_changed(self, text):
        self.password_text = text
    
    def eventFilter(self, obj, event):
        if event.type() == event.HoverEnter:
            obj.setStyleSheet("background-color: #4a148c; color: #ffffff; padding: 10px; border-radius: 5px; font-size: 16px;")
        elif event.type() == event.HoverLeave:
            obj.setStyleSheet("background-color: #6200ea; color: #ffffff; padding: 10px; border-radius: 5px; font-size: 16px;")
        return super().eventFilter(obj, event)

    def popUp(self):
        pass

class FrontPage:
    def introCoins(self):
        self.a = ["bitcoin", "ethereum", "cosmos"]
        self.b = []
        for i in self.a:
            r = requests.get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={i}").json()
            change = r[0]["market_cap_change_percentage_24h"]
            self.b.append(change)

if __name__ == "__main__":
    u = User()
    f = FrontPage()
    f.introCoins()
    app = QApplication(sys.argv)
    lw = LoginWidget()
    lw.show()
    sys.exit(app.exec_())
    