import pywhatkit
import datetime
import time

contacts = ['YOUR_NUMBERS_CONTACT_LIST']

# Set message to be sent
message = "YOUR_DEFAULT_MESSAGE"

# Get current hour and minutes and add 60 seconds
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute + 1

# Send the message to each contact
for i, contact in enumerate(contacts):
    pywhatkit.sendwhatmsg(contact, message, hour, minute + i, 7, True, 3)
    time.sleep(max(0, 7 - 3))