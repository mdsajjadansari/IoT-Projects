import requests
import json
import time
from boltiot import Bolt
import conf, conf_sms, conf_mail
from boltiot import Sms, Bolt
from boltiot import Email, Bolt


def get_bitcoin_price():
   URL = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,INR" # REPLACE WITH URL
   response = requests.request("GET", URL)
   response = json.loads(response.text)
   current_price = response["USD"]
   return current_price  
   
mybolt = Bolt(conf.bolt_api_key, conf.device_id)
sms=Sms(conf_sms.SID, conf_sms.AUTH_TOKEN, conf_sms.TO_NUMBER, conf_sms.FROM_NUMBER)
mailer=Email(conf_mail.MAILGUN_API_KEY, conf_mail.SANDBOX_URL, conf_mail.SENDER_EMAIL, conf_mail.RECIPIENT_EMAIL)

def get_bitcoin_price():
   try:
   	URL = "https://min-api.cryptocompare.com/data/xxxxxxxxxxxxxxxxxxx=USD,JPY,INR" # REPLACE WITH URL we got from min-api.cryptocompare.com
   	response = requests.request("GET", URL)
   	response = json.loads(response.text)
   	current_price = response["USD"]
   	return current_price
   except Exception as e:
        print("Something went wrong when returning the sensor value")
        print(e)
        return -999
def send_telegram_message(message):
    """Sends message via Telegram"""
    url = "https://api.telegram.org/" + conf.telegram_bot_id + "/sendMessage"
    data = {
        "chat_id": conf.telegram_chat_id,
        "text": message
    }
    try:
        response = requests.request(
            "POST",
            url,
            params=data
        )
        print("This is the Telegram URL")
        print(url)
        print("This is the Telegram response")
        print(response.text)
        telegram_data = json.loads(response.text)
        return telegram_data["ok"]
    except Exception as e:
        print("An error occurred in sending the alert message via Telegram")
        print(e)
        return False
while True:

    current_price = get_bitcoin_price()
    print("The current Temperature is:", current_price)
    

    if current_price == -999:
        print("Request was unsuccessfull. Skipping.")
        time.sleep(10)
        continue
    

    if current_price <= conf.threshold:
        print("Alert! Current Bitcoin value has decreased ")
        print("Sending Telegram Alert.....")
        message = "Alert! Current Bitcoin value has decreased " + str(conf.threshold) + \
                  ". The current Bitcoin value is " + str(current_price)
        telegram_status = send_telegram_message(message)
        print("This is the Telegram status:", telegram_status)
        
        print(" Sending SMS Alert....")
		response_sms = sms.send_sms(" Alert! Current Bitcoin value has decreased ")
		print("Response From Twilio" +str(response_sms))
		print("SMS Status : " +str(response_sms.status))
		
		print("Sending Email Alert....")
		response_email = mailer.send_email( " Alert", "Current Bitcoin value has decreased ")
		email_response_text = json.loads(response_email.text)
		print("Response received from Mailgun is: " + str(email_response_text['message']))


    time.sleep(30) 

