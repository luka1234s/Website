from deta import Deta
import datetime
key_to_dbs="a0pveadf4gi_64Dem19iPLF2jwoMCM63oK4q2HgcSqAN"
#Intitializing the the Deta object
deta = Deta(key_to_dbs)
db = deta.Base("user_details")
drive = deta.Drive("lukecpukec")

def input_info(full_name, email, dob):
    return db.put({"full_name": full_name, "email": email, "date_of_birth": str(dob)})

def fetch_info():
    result= db.fetch()
    return result.items()

def get_drive(name, path):
    return drive.put(name, path)

def get_item(full_name):
    return db.get(full_name)
