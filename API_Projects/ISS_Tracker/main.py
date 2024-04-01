import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 6.603450
MY_LONG = 3.304977

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    'formatted':0,
}

def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
    sunset = data['results']['sunset'].split('T')[1].split(':')[0]
    timenow = datetime.now().hour
    if timenow >= sunset or timenow <= sunrise:
        return True

def is_iss_overhead():
    response = requests.get(url="http://api.com-notify.org/iss-now.json", params=parameters)
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]['latitude'])
    iss_lng = float(data["iss_position"]['longitude'])

    if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LONG-5 <= iss_lng <= MY_LONG+6:
        return True


print("Sucess!!!!!\n\nWaiting.................")

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        my_email = 'carlosmark894@gmail.com'
        pswd = 'oftc srpl tiho jhyi '
        print("Email is about to be sent")
        
        connection = smtplib.SMTP_SSL("smtp.gmail.com")
        connection.login(my_email, pswd)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='ukwedjedimeji@gmail.com',
            msg = 'Subject: Look UP\n\nThe ISS is above your house'
        )
