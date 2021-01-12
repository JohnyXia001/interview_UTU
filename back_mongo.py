import pymongo
import csv

class database:
    def __init__(self):
        self.myclient = pymongo.MongoClient(
        "mongodb+srv://1262947004:199701xkz@cluster0.dmjoc.mongodb.net/Cluster0?retryWrites=true&w=majority")
        self.mydb = self.myclient["mydatabase"]
        self.mycol = self.mydb["coin_history"]
        self.crypto_type = ['tezos', 'bitcoin', 'bnb', 'bitcoin-cash', 'cardano']

    def upload_mongodb(self,file_name):
        self.mycol.drop()

        header = ["Currency", "Date", "Open", "High", "Low", "Close", "Volume", "Market Cap"]
        csvfile = open(file_name, 'r')
        reader = csv.DictReader(csvfile)

        for line in reader:
            row = {}
            for field in header:
                row[field] = line[field]
            x = self.mycol.insert_one(row)
            print(row)
        print(self.myclient.list_database_names())

    def measure(self,coin_name):
        myquery = {"Currency": coin_name}
        mydoc = back.mycol.find(myquery)
        result = list(mydoc)
        market_cap = int(float(result[0]["Market Cap"]))
        volume = int(float(result[0]["Volume"]))

        close_price_today = float(result[0]["Close"])
        close_price_24h = float(result[1]["Close"])
        d_24h = (close_price_today - close_price_24h) / close_price_24h
        d_24h = "%.2f" % (d_24h * 100) + "%"

        close_price_7d = float(result[7]["Close"])
        d_7d = (close_price_today - close_price_7d) / close_price_7d
        d_7d = "%.2f" % (d_7d * 100) + "%"

        close_price_1m = float(result[30]["Close"])
        d_1m = (close_price_today - close_price_1m) / close_price_1m
        d_1m = "%.2f" % (d_1m * 100) + "%"

        # print(coin_name,close_price_today,d_1m,d_7d,d_24h,volume,market_cap)
        return [coin_name, close_price_today, d_1m, d_7d, d_24h, volume, market_cap]

    def measure_all_crypto(self):
        final = []
        for name in self.crypto_type:
            final.append(self.measure(name))
        final = sorted(final,key=lambda x: x[-1],reverse=True)

        for line in final:
            print(line)
        return final

file_name = 'crypto_historical_data.csv'
back = database()
back.measure_all_crypto()

# ['tezos', 1.25, '40.45%', '-0.79%', '-3.10%', 46048752, 824588509]