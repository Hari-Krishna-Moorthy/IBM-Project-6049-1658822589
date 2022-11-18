from cloudant.client import Cloudant 

USERNAME = "2a3897c5-4813-4d4e-a46d-1075cbe1c9ca-bluemix"
APIKEY = "jt9RIMKSEUgXJLvbSivOhaQPbYG3UnOi1tmt_j2ycIIN"
CONNECT = True
DBNAME = "my_database"

client = Cloudant.iam(USERNAME, APIKEY, connect=CONNECT)
my_database = client.create_database(DBNAME)
print("DB is successfully created")
