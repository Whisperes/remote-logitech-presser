''' send request to server and get response'''
import requests
import sys

from config import settings
from utils.logger import logger

# get response  and print   response
def send_get(key: str):
   response = requests.get(f'{settings["URL"]}/key/{key}')
   logger.info(response.text)
   return response.status_code


if __name__ == "__main__":
    send_get(sys.argv[1])b