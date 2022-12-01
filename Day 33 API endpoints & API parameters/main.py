import requests
from datetime import datetime
import smtplib



MY_LAT = 39.577261 # Your latitude
MY_LONG = 2.627258 # Your longitude
MY_EMAIL = "EXAMPLE@GMAIL.COM"
MY_PASSWORD = "000000"

''''IN ORDER TO KNOW IF WE CAN SEE THE ISS   
WE ARE GOING TO MAKE AN APP THAT TELLS US:
1. IF ITS OVER OUR HEAD (VISIBLE FOR OUR LOCATION)
2. IF ITS NIGHT (YOU CAN'T SEE THE SATELITE DURING DAYTIME)
3. IF BOTH OF THEM ARE TRUE, WE ARE GOING TO RECIVE AN EMAIL TELLING US SO'''

def is_iss_overhead():
    # API REQUEST
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    # GET ISS SATELITE LONG AND LAT
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # CHECKING IF IT'S OVER OUR HEAD
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_night():
    # WE GET THE SUNRISE AND SUNSET TIME FOR OUR LOCATION   
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

if is_iss_overhead and is_night:
    connection = smtplib.SMPT("smpt.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
    )