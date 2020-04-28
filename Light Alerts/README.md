# Light Alerts

I have completed my Temperature Monitor Project which send alert Sms and email alert when the temperature crosses its threshold with the help of Bolt Module and Bolt Cloud using python3 language. Here the Bolt Cloud will send an email as well as SMS when light goes off (means its value declease from value 10) on LDR connected to Bolt Module.
To send SMS alert I have used Twilio (https://www.twilio.com) And For Email alert I have used Mailgun (https://www.mailgun.com)

First of All change credentials of `email_conf.py` and `sms_conf.py` according to your Mailgun and Twilio Account.

## Here the circuit connection will be something like this:

Hardware Required

    1 x Bolt IoT Module
    1 x Micro USB Cable
    1 x LDR (2 legged devicewith a red wave pattern disk on top)
    1 x 10k Ohm Resistor (brown black orange color code)

The resistance of an LDR varies inversely with light, i.e., the resistance decreases as the intensity of light falling on the LDR increases.
Connecting the LDR Circuit to the Bolt

Connect the LDR to Bolt as shown in image below. Note: There is no positive or negative for this and the 10k Ohm resistor. Also, make sure the Bolt module is not powered on while making connections. Always make it a habit to power off the circuit while making connections for your own and the circuit's safety. Double-check all connections before turning it on.

Here are the steps for making the hardware connections:

    Step 1: Insert one lead of the LDR into the Bolt Module's 3v3 Pin.
![](https://cdn.fs.teachablecdn.com/ADNupMnWyR7kCWRvm76Laz/resize=width:1500/https://www.filepicker.io/api/file/ONS4lPnhRnmRHNCshDDV)

    Step 2: Insert other lead of the LDR into the A0 pin
![](https://cdn.fs.teachablecdn.com/ADNupMnWyR7kCWRvm76Laz/resize=width:1500/https://www.filepicker.io/api/file/LyuLA4JMTSy9NSx3qAG9)

    Step 3: Insert one leg of the 10k Ohm resistor into the GND pin
![](https://cdn.fs.teachablecdn.com/ADNupMnWyR7kCWRvm76Laz/resize=width:1500/https://www.filepicker.io/api/file/W6NJDEZKRNK8C4R6wjD8)

    Step 4: Insert the other leg of the resistor also into the A0 pin

![](https://cdn.fs.teachablecdn.com/ADNupMnWyR7kCWRvm76Laz/resize=width:1500/https://www.filepicker.io/api/file/4JIf9WRJWvMxZvHaWAZA)

    Warning!! Make sure that at no point do the 3.3V (or even 5V) and GND pins or wires coming out of them touch each other. If you short power to Ground without a resistor even accidentally, the current drawn might be high enough to destroy the Bolt module 

Thus, we are effectively measuring the voltage across the 10k Ohm Resistor and the final circuit should look like the image below:
![](https://cdn.fs.teachablecdn.com/ADNupMnWyR7kCWRvm76Laz/resize=width:1500/https://www.filepicker.io/api/file/MH3Py6pKQpOuAiNGokag)

    Now connect your module to your cloud and Run
> python3 Light_Alerts.py

This will print the reading and if the reading goes below 10 (threshold vaue which is changeable) it will send an Alert to Monile number as Well as Email Id.
