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
        r = requests.get(f"https://api.coingecko.com/api/v3/coins/{id}/history?date={self.day}-{self.month}-{self.year}?x_cg_demo_api_key=CG-TFTmKujK1CwFn4B2KXA4hGPR", headers=self.header).json()
        r = round(r["market_data"]["current_price"]["usd"],2)
        return r

    def calc(self,id1,id2):
        id1 = id1.lower()
        id2 = id2.lower()
        r1 = requests.get(f"https://api.coingecko.com/api/v3/coins/{id1}/history?date={self.day}-{self.month}-{self.year}?x_cg_demo_api_key=CG-TFTmKujK1CwFn4B2KXA4hGPR", headers=self.header).json()
        r2 = requests.get(f"https://api.coingecko.com/api/v3/coins/{id2}/history?date={self.day}-{self.month}-{self.year}?x_cg_demo_api_key=CG-TFTmKujK1CwFn4B2KXA4hGPR", headers=self.header).json()
        id1_market_cap = int(r1["market_data"]["market_cap"]["usd"])
        id2_market_cap = int(r2["market_data"]["market_cap"]["usd"])
        multiplier = round(max(id1_market_cap,id2_market_cap) / min(id1_market_cap,id2_market_cap),2)
        if id1_market_cap < id2_market_cap:
            price = int(r1["market_data"]["current_price"]["usd"]) * multiplier
            return [id1,id2,price,multiplier]
        else:
            price = int(r2["market_data"]["current_price"]["usd"]) * multiplier
            return [id2,id1,price,multiplier]