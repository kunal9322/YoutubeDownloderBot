# by <@kaif-00z>

from decouple import config

try:
    API_ID = config("API_ID", cast=int)
    API_HASH = config("API_HASH","12bbd720f4097ba7713c5e40a11dfd2a")
    BOT_TOKEN = config("BOT_TOKEN","6020053428:AAGaKdIalVe2UDk1PDzFc5Rz5E_bBfF6Dw8")
    OWNER = config("OWNER_ID", cast=int)

except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
