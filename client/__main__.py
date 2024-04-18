''' send request to server and get response'''

import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
os.chdir("..")
print (os.path.abspath(os.curdir))


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
    send_get(sys.argv[1])