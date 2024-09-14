from environs import Env

env = Env()
env.read_env()

# TEST_GROUP = env.str("TEST_GROUP")
BOT_TOKEN = env.str("BOT_TOKEN")
BIG_ADMIN = env.str("BIG_ADMIN")
ADMINS = env.list("ADMINS")

DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")
