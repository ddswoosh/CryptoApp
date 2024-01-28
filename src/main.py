import json,requests
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
