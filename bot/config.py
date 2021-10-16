# by <@kaif-00z>

from decouple import config


try:
    API_ID = config("API_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    OWNER = config("OWNER_ID", cast=int)

except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
