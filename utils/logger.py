'''
Setup logger for whole project
'''

import logging
import sys
import os
from datetime import datetime

#init logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#setup handler
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

