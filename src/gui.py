from PyQt5.QtWidgets import (
    QGraphicsView, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QWidget, QHBoxLayout, QApplication,
    QMessageBox, QTabWidget, QStackedWidget, QSizePolicy,
    QGraphicsScene, QTableWidget, QTableWidgetItem, QHeaderView,
    QSizePolicy, QScrollArea, 
)
from PyQt5.QtCore import Qt, QObject, QDateTime, QTimer, QEvent
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QColor, QCursor
from auth import User
import requests
import sys
import os
import math
from main import Get

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
        self.username_input.textChanged.connect(self.onUsernameChanged)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("background-color: #42445a; color: #bb86fc; padding: 10px; border-radius: 5px; text-align: center;")
        self.password_input.setAlignment(Qt.AlignCenter)
        self.password_input.setFixedWidth(input_width)
        self.password_input.textChanged.connect(self.onPasswordChanged)

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
        login_button.clicked.connect(self.onLoginClicked)
        login_button.installEventFilter(self)

        register_button = QPushButton("Register", self)
        register_button.setStyleSheet("background-color: #003366; color: #ffffff; padding: 10px; border-radius: 5px; font-size: 16px;")
        register_button.clicked.connect(self.onRegisterClicked)
        register_button.installEventFilter(self)

        layout.addSpacing(10)  

        layout.addWidget(login_button)
        layout.addWidget(register_button)

    def onLoginClicked(self):
        l = u.login(self.username_text, self.password_text)

        if l != 0:
            self.main_widget = MainWidget()
            self.main_widget.show()
            self.close()
        else:
            self.popUp("Invalid username or password. Please register your account.")
            return
           
        
    def onRegisterClicked(self):
        l = u.register(self.username_text,self.password_text)
        if l != 0:
            self.popUp(
                "Your account has been created \n"
                "Please login."
                       )
            return
        
    def onUsernameChanged(self, text):
        self.username_text = text

    def onPasswordChanged(self, text):
        self.password_text = text
    
    def eventFilter(self, obj, event):
        if event.type() == event.HoverEnter:
            obj.setStyleSheet("background-color: #4a148c; color: #ffffff; padding: 10px; border-radius: 5px; font-size: 16px;")
        elif event.type() == event.HoverLeave:
            obj.setStyleSheet("background-color: #6200ea; color: #ffffff; padding: 10px; border-radius: 5px; font-size: 16px;")
        return super().eventFilter(obj, event)

    def popUp(self, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Authentication Error")
        msg_box.setText(message)
        msg_box.exec_()

class FrontPage:
    def introCoins(self):
        self.a = ["bitcoin", "ethereum", "cosmos"]
        self.b = []
        for i in self.a:
            r = requests.get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={i}&x_cg_demo_api_key=CG-TFTmKujK1CwFn4B2KXA4hGPR").json()
            change = r[0]["market_cap_change_percentage_24h"]
            self.b.append(change)

class WalletPage(QWidget):
    def __init__(self):
        super().__init__()
        self.arr = []
        self.coin_text = ""
        self.quantity_text = ""

        primary_background_color = "#1f1f2e"
        input_background_color = "transparent"
        input_text_color = "#bb86fc"
        input_border_color = "#bb86fc"
        button_background_color = "#6200ea"
        button_text_color = "#ffffff"
        button_hover_color = "#7a29d2" 

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)

        self.coin_name_input = QLineEdit(self)
        self.coin_name_input.setPlaceholderText("Coin Name (eg. bitcoin | ethereum)")
        self.coin_name_input.setStyleSheet(
            f"background-color: {input_background_color}; color: {input_text_color}; padding: 10px; border: 1px solid {input_border_color}; border-radius: 5px;")
        self.coin_name_input.textChanged.connect(self.onCoinChanged)

        self.coin_amount_input = QLineEdit(self)
        self.coin_amount_input.setPlaceholderText("Quantity")
        self.coin_amount_input.setStyleSheet(
            f"background-color: {input_background_color}; color: {input_text_color}; padding: 10px; border: 1px solid {input_border_color}; border-radius: 5px; text-align: center")
        self.coin_amount_input.textChanged.connect(self.onQuantityChanged)

        self.add_coin_button = QPushButton("Add To Portfolio", self)
        self.add_coin_button.setStyleSheet(
            f"background-color: {button_background_color}; color: {button_text_color}; padding: 10px; border-radius: 5px; font-size: 16px;")
        self.add_coin_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_coin_button.clicked.connect(self.addPortfolio)

        self.coin_name_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.coin_amount_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout.addWidget(self.coin_name_input)
        layout.addWidget(self.coin_amount_input)
        layout.addWidget(self.add_coin_button)

        self.coin_list_layout = QVBoxLayout()
        coin_scroll_area = QScrollArea()
        coin_scroll_area.setWidgetResizable(True)
        coin_scroll_area.setStyleSheet(f"background-color: {primary_background_color};")
        coin_scroll_area.setWidget(QWidget())
        coin_scroll_area.widget().setLayout(self.coin_list_layout)

        layout.addWidget(coin_scroll_area, 1)

        total_layout = QHBoxLayout()
        total_label = QLabel("Total:", self)
        total_label.setStyleSheet(f"font-size: 18px; color: {input_text_color};")
        self.total_amount_label = QLabel(self)
        self.total_amount_label.setStyleSheet(f"font-size: 18px; color: {input_text_color}; margin-left: 5px;")

        total_layout.addWidget(total_label)
        total_layout.addWidget(self.total_amount_label)
        total_layout.addStretch()
        total_label.setAlignment(Qt.AlignCenter)

        layout.addLayout(total_layout)

        layout.setAlignment(Qt.AlignTop)
        self.setStyleSheet(f"background-color: {primary_background_color};")

    def onCoinChanged(self, text):
        self.coin_text = text

    def onQuantityChanged(self, text):
        self.quantity_text = text
    
    def addPortfolio(self):
        if self.coin_text:
            quantity = float(self.quantity_text)
            if 0 < quantity <= 1000000:
                g = Get()
                price = g.grab(self.coin_text)
                self.coin_total = price * quantity
                self.arr.append(round(self.coin_total, 2))
                self.addCoinToList(self.coin_text.upper(), quantity, math.floor(self.coin_total))
            else:
                self.popUp("Please enter a quantity between 1 and 1,000,000")
        else:
            self.popUp("Please enter a valid cryptocurrency name. This must be the full name like Bitcoin, Ethereum, or Solana.")

    def addCoinToList(self, coin, quantity, total):
        arr = []
        arr.append(total)
        coin_label = QLabel(f"{coin} ----- Quantity: {quantity}                                                                              Total: ${total}")
        coin_label.setStyleSheet(f"color: #ffffff; font-size: 16px;")
        self.coin_list_layout.addWidget(coin_label)
        total = 0
        for i in range(len(self.arr)):
            total += self.arr[i]
        self.total_amount_label.setText("$" + str(total)) 

    def popUp(self, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.exec_()


class CalculatorPage(QWidget):
    def __init__(self):
        super().__init__()

        self.coin1_value = ""
        self.coin2_value = ""

        layout = QVBoxLayout(self)
        self.coin1_input = QLineEdit(self)
        self.coin1_input.setPlaceholderText("Coin 1")
        self.coin1_input.setStyleSheet("background-color: #42445a; color: #bb86fc; padding: 10px; border-radius: 5px; text-align: center;")
        self.coin1_input.textChanged.connect(self.onCoin1Changed)

        self.coin2_input = QLineEdit(self)
        self.coin2_input.setPlaceholderText("Coin 2")
        self.coin2_input.setStyleSheet("background-color: #42445a; color: #bb86fc; padding: 10px; border-radius: 5px; text-align: center;")
        self.coin2_input.textChanged.connect(self.onCoin2Changed)

        self.calculate_button = QPushButton("Calculate", self)
        self.calculate_button.setStyleSheet("background-color: #6200ea; color: #ffffff; padding: 10px; border-radius: 5px; font-size: 16px;")
        self.calculate_button.clicked.connect(self.onCalculateClicked)
        self.calculate_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.calculate_button.setMouseTracking(True)
        self.calculate_button.installEventFilter(self)

        self.result_label = QLabel("", self)
        self.result_label.setStyleSheet("color: #ffffff; font-size: 14px;")

        layout.addWidget(self.coin1_input, alignment=Qt.AlignCenter)
        layout.addWidget(self.coin2_input, alignment=Qt.AlignCenter)
        layout.addWidget(self.calculate_button, alignment=Qt.AlignCenter)
        layout.addWidget(self.result_label, alignment=Qt.AlignCenter)

    def eventFilter(self, obj, event):
        if obj == self.calculate_button:
            if event.type() == QEvent.Enter:
                self.calculate_button.setStyleSheet("background-color: #7a29d2; color: #ffffff; padding: 10px; border-radius: 5px; font-size: 16px;")
            elif event.type() == QEvent.Leave:
                self.calculate_button.setStyleSheet("background-color: #6200ea; color: #ffffff; padding: 10px; border-radius: 5px; font-size: 16px;")
        return super().eventFilter(obj, event)

    def onCoin1Changed(self, text):
        self.coin1_value = text
    
    def onCoin2Changed(self, text):
        self.coin2_value = text

    def onCalculateClicked(self):
        if not self.coin1_value or not self.coin2_value:
            self.popUp("Please enter a coin in both fields.")
        else:
            g = Get()
            new_price = g.calc(self.coin1_value, self.coin2_value)
            result_text = f"{new_price[0].upper()} with {new_price[1].upper()}'S market cap, puts 1 coin at ${new_price[2]} ({new_price[3]})x"
            self.coin2_input.setPlaceholderText(result_text)

            self.result_label.setText(result_text)
            self.result_label.setStyleSheet("color: #ffffff; font-size: 16px; background-color: #212121; padding: 10px; border-radius: 5px;")
    def popUp(self, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.exec_()

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 8500, 600)  
        self.setWindowTitle("Crypto App")
        self.setStyleSheet("background-color: #1f1f2e;")
        self.setWindowIcon(QIcon('Logos/bitcoin.png'))

        self.setMaximumWidth(850)
        self.setMaximumHeight(600)
        self.setMinimumWidth(850)
        self.setMinimumHeight(600)

        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignCenter) 

        self.tabs = QTabWidget(self)
        self.tabs.setStyleSheet("QTabBar::tab { color: #bb86fc; background-color: #6200ea; padding: 8px 20px; }"
                                "QTabBar::tab:selected { background-color: #4a148c; }"
                                "QTabWidget::pane { border: none; }")
        self.tabs.setTabPosition(QTabWidget.North)
        self.tabs.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.tabs.setMinimumWidth(800)

        self.pages = QStackedWidget(self)
        self.pages.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.wallet_page = WalletPage()
        self.calculator_page = CalculatorPage()

        self.pages.addWidget(self.wallet_page)
        self.pages.addWidget(self.calculator_page)

        self.tabs.addTab(self.wallet_page, self.createTabIcon("Logos/wallet_icon.png"), "Wallet")
        self.tabs.addTab(self.calculator_page, self.createTabIcon("Logos/calculator_icon.png"), "Calculator")

        main_layout.addWidget(self.tabs, alignment=Qt.AlignCenter)
        main_layout.addWidget(self.pages)

    def createTabIcon(self, icon_path):
        tab_icon = QPixmap(icon_path)
        tab_icon = tab_icon.scaledToWidth(30, mode=Qt.SmoothTransformation)
        return QIcon(tab_icon)
    
if __name__ == "__main__":
    u = User()
    f = FrontPage()

    f.introCoins()
    app = QApplication(sys.argv)
    lw = LoginWidget()
    lw.show()
    sys.exit(app.exec_())
    