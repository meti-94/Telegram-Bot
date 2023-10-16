#!/usr/bin/env python
import asyncio
import nest_asyncio
nest_asyncio.apply()



import logging
import os
from telegram import (
    ReplyKeyboardMarkup, 
    ReplyKeyboardRemove, 
    Update, 
    InlineKeyboardButton, 
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
)
from telegram.constants import ParseMode

from dal import *
db = UserDatabase()


from prompts import writing_email

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

from dal import *
INFO = {}
TIMEOUT = -2
CHOOSING, DEGREE, PROFESSOR, INSTITUTE, FIELD, APPLICANT, INTEREST, EXPERIENCE, ATTACHMENT, WRITING = range(10)
db = UserDatabase()

#####################
INITIAL_CREDIT = 1
INITIAL_MONEY = 0
TIMEOUT_COUNT = 180
#####################

degree_mapping = {
        'کارشناسی':'BS',
        'کارشناسی ارشد':'MS',
        'دکترا':'PHD',
    }
degree_reverse_mapping = {
        v:k for k,v in degree_mapping.items()
    }
