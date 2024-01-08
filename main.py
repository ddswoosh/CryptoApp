import os,json,requests

class Get:
    def __init__(self):
        self.url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin&x_cg_api_key=CG-TFTmKujK1CwFn4B2KXA4hGPR"
        self.auth = "CG-TFTmKujK1CwFn4B2KXA4hGPR"
        self.params = {}
        x = input(pyqtInput)

    def grab(self):
        a = []
        symbol = x
        self.params["symbol"] = symbol.lower()
        r = requests.get(self.url).json()
        return r[0][_]
        # i = 0
        # while i < cg.requestmax:
        #     if cg.request == symbol1:
        #         a[i] == 0

    def insert(self):
        pass

class Login:
    def __init__(self,user,password):
        self.user = user
        self.passwrod = password
    
    def check(self):
        if Login(user,password) in db:
            return True
        self.login()
    
    def login(self):
        if self.check() == True:
            pass
            #run next gui
l = Login()
g = Get()
if __name__ in "__main__":
    g.grab()
    l.check()
