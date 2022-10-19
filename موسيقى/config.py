##Config

from os import getenv
from dotenv import load_dotenv

load_dotenv()
get_queue = {}
SESSION_NAME = getenv('SESSION_NAME', 'BAAH8Tg_joDn_8EbPjzAxeWx96KTFqiQa_qsCP_V22vanhN-DsrL2UPn213fhgDHCfS0JQfSSdQlxqgRPs5I1XoYjcZkPaCe_UnJVwI_CFfvK62r87f3GapL9dSJmF6gXShL9lGC117eh8SwXgiBcaUI6dlpy_-NccPbrLlb7Jk4HP6X-09O0ki9wtMU_cGRVjfowAf4BwXYJkRfVZcxSqWZ5OBIekup5WaeQV97mnilkFdYXYmP4zKSkTfhQuSaPswpBv-TTWAtoHVYkQad8q0ROX6G4TF2KKV8KbIYKeGwge2jY1nJ_-ub3zmVvM3MnvLn093bedop-s3NRQsjkE8FAAAAAUx1Wo4A')
BOT_TOKEN = getenv('BOT_TOKEN'   , "5761526686:AAHsgLMa4esjIJckXV1SboOC505bu1SOo-8")
API_ID = int(getenv('API_ID', "17929336"))
API_HASH = getenv('API_HASH'   , "2cbbc91b3a665a8fe862657625492790")
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '30'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '').split())
MONGO_DB_URI = getenv("MONGO_DB_URI"   , "mongodb://mongo:bJw7qSyg16WEGlrphSbV@containers-us-west-21.railway.app:6352")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', 'MUSIC_2RUSSIA').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001680345766'))
ASS_ID = int(getenv("ASS_ID", '2130437611'))
OWNER_ID = list(map(int, getenv('OWNER_ID', '5422127338').split()))
BOT_IMG = getenv("BOT_IMG"   , "https://telegra.ph/file/2d1372d13b7b8f496b0d1.jpg")
GROUP = getenv("GROUP", "RUSSIA_TEST")
CHANNEL = getenv("CHANNEL", "X_x_RUSSIA_x_X")
