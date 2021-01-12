import csv


class crypto:
    def __init__(self, file_name):
        self.file = self.load_file(file_name)
        self.crypto_type = ['tezos','bitcoin','bnb','bitcoin-cash','cardano']

    def load_file(self,file_name):
        with open(file_name, newline='') as csvfile:
            spamreader = list(csv.reader(csvfile))
        return spamreader

    def measure(self,coin_name):
        data = [row for row in self.file if row[0]==coin_name]
        market_cap = int(float(data[0][-1]))
        volume = int(float(data[0][-2]))

        close_price_today = float(data[0][5])
        close_price_24h = float(data[1][5])
        d_24h = (close_price_today-close_price_24h)/close_price_24h
        d_24h = "%.2f" % (d_24h*100)+"%"

        close_price_7d = float(data[7][5])
        d_7d = (close_price_today - close_price_7d) / close_price_7d
        d_7d = "%.2f" % (d_7d * 100) + "%"

        close_price_1m = float(data[30][5])
        d_1m = (close_price_today - close_price_1m) / close_price_1m
        d_1m = "%.2f" % (d_1m * 100) + "%"

        # for line in data:
        #     print(line)

        # print(coin_name,close_price_today,d_1m,d_7d,d_24h,volume,market_cap)
        return [coin_name,close_price_today,d_1m,d_7d,d_24h,volume,market_cap]

    def measure_all_crypto(self):
        final = []
        for name in self.crypto_type:
            final.append(self.measure(name))
        final = sorted(final,key=lambda x: x[-1],reverse=True)

        for line in final:
            print(line)
        return final


file_name = 'crypto_historical_data.csv'
process = crypto(file_name)
process.measure_all_crypto()
