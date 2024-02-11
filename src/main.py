import json,requests,math,time
class Get:
    def __init__(self):
        self.header = {
            "accept" : "application/json"
        }
        ct = time.localtime()
        self.year = ct.tm_year
        self.month = ct.tm_mon
        self.day = ct.tm_mday

    def grab(self,id):
        id = id.lower()
        r = requests.get(f"https://api.coingecko.com/api/v3/coins/{id}/history?date={self.day}-{self.month}-{self.year}", headers=self.header).json()
        r = r["market_data"]["current_price"]["usd"]
        r = round(r,2)
        return r

    def insert(self):
        pass

