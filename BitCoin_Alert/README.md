#  Bitcoin Price Alerting System <img src="https://thumbs.gfycat.com/IllSharpCod-max-1mb.gif" width="60" height="55"></img>

<img src="https://bitcoinexchangeguide.com/wp-content/uploads/2019/03/Bitcoin-Network-Difficulty-Reaches-New-High-in-More-than-Three-Months-Will-BTC-Price-Follow.jpg"></img>

This assignment is based on the popular cryptocurrency called Bitcoin. I have build a Bitcoin Price Alert System with the help of `Bolt IoT` and `cryptocompare.com`. Here I have writen a Python program that checks the current price of Bitcoin and send alerts via sms, E-mail & Telegram. If Bit coin price is decreased than the selling price which I have set as a `Threshold Value` in the file named `conf.py`

To build the Bitcoin Price Alerting system, we will require a method to find the current price of Bitcoin by writing a Python program. I have used the website https://min-api.cryptocompare.com to get the price of Bitcoin. It is a very popular site that provides APIs using which you can fetch various cryptocurrency related data. You don’t need  to create an account on the site to get the Bitcoin values. On this website all currencies are called as symbols or “sym” in short. I have used the Single Symbol Price API to get the price of Bitcoin in USD.

Here is the documentation of the Single Symbol Price API: https://min-api.cryptocompare.com/documentation?key=Price&cat=SingleSymbolPriceEndpoint.

The Python program `Bitcoin.py` will do the following

  * Fetch the current price of Bitcoin every 30 seconds using the Single Symbol Price API in USD.
  * Check if the current price returned by the API is greater than or less than the selling price defined in `conf.py` file as `threshold`.
  * If the current price is less than the selling price, the program should send alerts via sms,E-mail & Telegram

> To send SMS alert I have used Twilio (https://www.twilio.com).
> For Email alert I have used Mailgun (https://www.mailgun.com)
> For Telegram Alert I have used the `Bot father` Option of Telegram to make a Bot and added it to a new Channel as Admin.

## We require some additional Python libraries to be installed to run this project. 
        Make sure that you have installed the following libraries before your write the Python program.

> sudo apt-get update

> sudo pip3 install boltiot

> sudo pip3 install pyOpenSSL ndg-httpsclient pyasn1

> sudo pip3 install 'requests[security]'

<p> Author : iamsajjadansari@gmail.com </p>
