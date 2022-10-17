import telepot 
import requests 
from datetime import datetime
from timeloop import Timeloop
from datetime import timedelta
from twilio.rest import Client
#code added by Aakshita

tl = Timeloop()

@tl.job(interval=timedelta(seconds=60))
def run_tasks():
    ticker = "AMZN"
    real_time_data = getStockData(ticker)
    textMessage = generateMessage(real_time_data)
    sendMessage(textMessage)
    
tl.start(block=True)
