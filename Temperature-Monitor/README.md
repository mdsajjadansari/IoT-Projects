# Temperature-Monitor
I have completed my Temperature Monitor Project which send alert Sms and email alert when the temperature crosses its threshold with the help of Bolt Module and Bolt Cloud using python3 language.

To send SMS alert I have used Twilio (https://www.twilio.com)
And For Email alert I have used Mailgun (https://www.mailgun.com)


## Requirements:
* The Bolt Wifi module 
* The Bolt cloud
* 3 female to male wire
* Temperature Sensor: LM35 sensor

### Connecting the LM35 sensor to the Bolt module

![LM35](https://cdn.fs.teachablecdn.com/resize=width:1500/8oB9WdMSy2vBpwIKEYK6)

In the above image VCC is connected to the red wire, Output is connected to the orange wire and Gnd is connected to the brown wire. Using male to female wire connect the 3 pins of the LM35 to the Bolt Wifi Module as follows:

    VCC pin of the LM35 connects to 5v of the Bolt Wifi module.
    Output pin of the LM35 connects to A0 (Analog input pin) of the Bolt Wifi module.
    Gnd pin of the LM35 connects to the Gnd.
![](https://cdn.fs.teachablecdn.com/resize=width:1500/G6j1stIQDOBd6kRffdyw)

The final circuit should look like the image below:
![](https://cdn.fs.teachablecdn.com/resize=width:1500/Ig2OOt38Tn28UQro2CT0)

Now connect you Module with your cloud, in the sms_conf.py file change your credentials with respect to your Twilio Account Details. and in email_conf.py change your credentials with respect to your Mailgun Account details such as API Keys, Device Id and SID etc.
 
 the run the below code for sms alert
 > python3 temp_sms.py
 
 and run the below code for email alert
 > python3 temp_email.py
