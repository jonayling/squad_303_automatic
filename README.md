## Squad 303 - Russian War information SMS automation

The following simple Python scripts allow automation of the process of sending SMS messages informing Russian citizens of the crimes being carried out by the Kremlin leadership during the 2022 war in Ukraine. The aim is to break through Putin's wall of lies and censorship and make ordinary Russian citizens aware of the truth.

Squad 303 provide an interface for generating these messages, and a database of phone numbers to send them to, at [https://1920.in/](https://1920.in/).

This script automates the process, by

- Retrieving the telephone numbers from the squad 303 API
- Sending an SMS message using the [Twilio SMS API](https://www.twilio.com/sms)

### Dependencies

You will need:

- A basic python 3 environment
- A twilio account, with a phone number registered that can send SMS. Make sure you enable +7 (Russia) is the Georestriction. Obtain an authorization token `auth_token` from Twilio.
- A `cf_clearance` cookie from https://1920.in/. Get this by visiting in your browser, press F12 and inspect the cookies sent for the requests.

Populate the Twilio `account_sid` and `auth_token`, the phone number you wish to use, and the `cf_clearance` cookies in `config.py`.

### Running

Run **main.py** to start sending messages. By default a message to a new number is send once every 10 seconds.

