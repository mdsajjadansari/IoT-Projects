import sms_conf, email_conf
from boltiot import Sms, Bolt
from boltiot import Email, Bolt
import json, time

minimum_limit = 10
maximum_limit = 220

mybolt=Bolt(conf_sms.API_KEY,conf_sms.DEVICE_ID)
sms=Sms(conf_sms.SID, conf_sms.AUTH_TOKEN, conf_sms.TO_NUMBER, conf_sms.FROM_NUMBER)
mailer=Email(conf_mail.MAILGUN_API_KEY, conf_mail.SANDBOX_URL, conf_mail.SENDER_EMAIL, conf_mail.RECIPIENT_EMAIL)

while True:
	print(" Receiving Data... ")
	response = mybolt.analogRead('A0')
	data = json.loads(response)
	print (" Received data value is :  " +str(data['value']))
	try:
		sensor_value=int (data['value'])
		if sensor_value< minimum_limit:
			print(" Light is Switched off ")
			response_sms = sms.send_sms(" Light is Switched OFF ")
			response_email = mailer.send_email( " Alert", "Light is Switched OFF ")
			print("Response From Twilio" +str(response_sms))
			print("SMS Status : " +str(response_sms.status))
			email_response_text = json.loads(response_email.text)
			print("Response received from Mailgun is: " + str(email_response_text['message']))
		else :
			print (" Light is Switched On ")
	except Exception as e:
		print( "Error Occured : Details Below ")
		print (e)
	time.sleep(10) 
		
 
