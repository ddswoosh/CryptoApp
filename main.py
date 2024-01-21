import os,json,requests

class Get:
    def __init__(self):
        self.url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin"
        self.auth = "CG-TFTmKujK1CwFn4B2KXA4hGPR"
        self.params = {}
        self.x = input("Enter")

    def grab(self):
        a = []
        symbol = self.x
        self.params["symbol"] = symbol.lower()
        r = requests.get(self.url).json()
        return r[0]

    def insert(self):
        pass

class User:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.override = False

    # def login(self):
    #     if self.override:
    #         if self.user and self.password in db:
    #             gui.run()
    #     else:
    #         if u(lw.username_text, lw.password_text) in db:
    #             pass
                # gui.run()

if __name__ in "__main__":
    u = User(1,2)
    g = Get()
    print(g.grab())
    