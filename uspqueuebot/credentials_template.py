## RENAME THIS FILE TO credentials.py

# This file contains all the security credentials for the bot.

# for debugging purposes
ADMIN_CHAT_ID = 0  # either int or str is fine

# for access to admin commands
ADMINS = {"admin_handle": ADMIN_CHAT_ID}

# for bot queue opening and closing (format: [year, month, day, hour, minute, second])
CHECK_TIME = False
START_TIME = [2023, 1, 1, 0, 0, 0]
END_TIME = [2023, 1, 1, 0, 0, 0]
