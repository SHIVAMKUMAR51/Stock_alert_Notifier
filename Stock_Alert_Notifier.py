import telepot 
import requests 
from datetime import datetime
from timeloop import Timeloop
from datetime import timedelta
from twilio.rest import Client
#code added by Shivam

def sendMessage(text):
    account_sid = "SID" # Your Account SID from twilio.com/console
    auth_token  = "Token" # Your Auth Token from twilio.com/console

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="XXX", #enter your verified phone number
        from_="+14255411934",
        body=text)

    print(message.sid)
#code added by Aakshita

tl = Timeloop()

@tl.job(interval=timedelta(seconds=60))
def run_tasks():
    ticker = "AMZN"
    real_time_data = getStockData(ticker)
    textMessage = generateMessage(real_time_data)
    sendMessage(textMessage)
    
tl.start(block=True)
