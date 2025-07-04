import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "....."))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4179ce15aab1f8396c0709347df1976a")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6013909736"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://ArtistKrishu:P32KSKiSBxa6vWxs@cluster0.6t3l158.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
