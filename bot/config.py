# by <@kaif-00z>

from decouple import config

try:
    API_ID = config("API_ID", "16743442")
    API_HASH = config("API_HASH","12bbd720f4097ba7713c5e40a11dfd2a")
    BOT_TOKEN = config("BOT_TOKEN","6020053428:AAGaKdIalVe2UDk1PDzFc5Rz5E_bBfF6Dw8")
    OWNER = config("OWNER_ID", "5885920877")

except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
