
# order the crypto by its market cap in descending mode

# display Price , 24h change difference , 7d change difference and
# 1month change difference, 24h Volume and Market Cap

# TODO:
# setup the data in Relational Database or Nosql Database
# retrieve data from a database or by calling an API
# process the data or build efficient computational logic
# display the processed data
import pymongo


myclient = pymongo.MongoClient("mongodb+srv://1262947004:199701xkz@cluster0.dmjoc.mongodb.net/Cluster0?retryWrites=true&w=majority")

# mydb = myclient["mydatabase"]
# print(myclient.list_database_names())
# mydb = client["sample_airbnb"]
# mycol = mydb["listingsAndReviews"]
#
# for x in mycol.find():
#   print(x)
