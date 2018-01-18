import httplib, urllib
from BusinessLayer.ParkinspotStateService import ParkingspotStateService
import urllib


def Vehicle():
    date = raw_input("What date would you like to park (YY-MM-DD HH:MM)")
    duration = raw_input("How long would you like to park (minutes)")
    GETRequest(date, duration);
    name = raw_input("What parkingspot would you like to take? ")
    licensePlate = raw_input("What is your cars license plate?")
    POSTRequest(name, date, duration, licensePlate)
    print("Making reservation for parkingspot " + str(name) + ", At date " + str(date) + " for " + str(duration) + " minutes!")

def GETRequest(date, duration):
    import httplib
    conn = httplib.HTTPConnection("131.155.239.0", "8085")
    #params = urllib.urlencode(dict({'starttime': date, 'duration': raw_input}))
    #url = "http://example.com/?a=text&q2=text2&q3=text3&q2=text4"
    f = {'duration': duration, 'starttime': date}

    conn.request("GET", "/ParkingSpotsAvailable/?" +  urllib.urlencode(f))
    res = conn.getresponse()
    print res.status, res.reason

def POSTRequest(name, date, duration, licensePlate):

    params = urllib.urlencode({'licensePlate': str(licensePlate), 'type': 'auto', 'parkingspot': name, 'duration': str(duration), 'starttime': str(date)})
    headers = {"Content-type": "application/x-www-form-urlencoded"}
    conn = httplib.HTTPConnection("131.155.239.0", "8085")
    conn.request("POST", "", params, headers)
    response = conn.getresponse()
    print("reservation for parkingspot " + str(name) + ", At date " + str(date) + " for " + str(duration) + " minutes succesfull!");
    print response.status, response.reason
    conn.close()



Vehicle();