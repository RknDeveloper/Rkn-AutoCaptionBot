# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr

import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Rkn_Bots(object):
    # Rkn client config
    API_ID = os.environ.get("API_ID", "")
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    #start_pic
    RKN_PIC = os.environ.get("RKN_PIC", "https://telegra.ph/file/21a8e96b45cd6ac4d3da6.jpg")


    # wes response configuration
    BOT_UPTIME = time.time()
    PORT = int(os.environ.get("PORT", "8080"))
    FORCE_SUB = os.environ.get("FORCE_SUB", "") 
    
    # database config
    DB_NAME = os.environ.get("DB_NAME", "AutoCaption_V05_Bot")     
    DB_URL = os.environ.get("DB_URL", "")

    #caption
    DEF_CAP = os.environ.get("DEF_CAP",
                             "<b><a href='telegram.me/Rkn_Bots'>{file_name} Telegram : @RknDeveloper\n\nForward the file before Downloading.</a></b>",
    )

    #sticker Id
    STICKER_ID = os.environ.get("STICKER_ID", "CAACAgIAAxkBAAELFqBllhB70i13m-woXeIWDXU6BD2j7wAC9gcAAkb7rAR7xdjVOS5ziTQE")

    #admin id
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
    

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr
