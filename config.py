import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "") 
    OWNER_ID = os.environ.get("OWNER_ID", "")
    DATABASE_URI = os.environ.get("DATABASE_URI", "")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "BQFzD0YAK2-CSLK77m3H5tTlOyRRmk5WXSaEieDW4iQ3sq73AUedHWR89kIDeDYoKC8MCcrHP_vRssKduPw2Pxq-0fEJ2saOBRltj7jdEYlrHHF-2JfyLnweO-cWB8HNZ8lbWHonh9nMc7McENva4jOnvVZ1VRrUuy4MnawSMtstecwCjoA_13vVRgu2Dzu8yBJxRlou9ltbdu02KWJFu01_6cDLWLP-Rj3wtbfzF8bGW1FNCvtgEhO-tE4jnLVI12JufTqq9k6Vv76RpugPCFfGNPxVSSFN8skmaMXtTCqSrdBWda_2ONIqgx0y2SsFx66eEi-H-9oSFQQJYHTg4wOZkp1yuQAAAAGA_uAYAA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", ""))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", None)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
