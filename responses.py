import logging
from telegram.ext import *
import responses
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


# Set up the Logging

logging.basicConfig(format='%(asctime)s - %(name)s -%(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')