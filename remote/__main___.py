'''Init main for project. FastApi is the main entry point for the project.
It accepts the symbol from request and press the button on keyboard.'''

import fastapi
from fastapi import FastAPI
import uvicorn

import pyautogui as gui

from utils.logger import logger

app = FastAPI()

# Description of the project for root url
@app.get("/")
async def root():
    return {"message": "Press key"}



#function, which press any button on keyboard on the machine using the pyautogui library
@app.get("/key/{key}")
async def key(key: str):
    try:
        for k in key:
            gui.press(k)
        logger.info(f"pressed {key}")
        return True
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=2750, log_level="debug")
