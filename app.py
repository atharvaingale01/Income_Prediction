from flask import Flask
from src.logger import logging
from src.exception import CustumException
import os,sys

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
    try:
        raise Exception("we are testing our custom file")
    except Exception as e:
        abc = CustumException(e,sys)
        logging.info(abc.error_message)
        return "Welcome to the Income Prediction APP"


if __name__ == "__main__":
    app.run(debug=True)