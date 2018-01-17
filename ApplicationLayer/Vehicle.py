import httplib, urllib



def Vehicle():
    name = input("What parkingspot would you like to take? ")
    data = input("What time and date would you like to park (YY-MM-DD,HH-MM")
    duration = input("How long would you like to park (minutes)")
    print("Making reservation for parkingspot " + str(name) + ", At date " + str(data) + "f r " + str(duration) + " minutes!")
    POSTRequest(name, data, duration)


def GETRequest():
    import httplib
    conn = httplib.HTTPConnection("131.155.238.86", "8085")
    conn.request("GET", "/ParkingSpotsAvailable")
    res = conn.getresponse()
    print res.status, res.reason

def POSTRequest(name, data, duration):
    params = urllib.urlencode({'licenseplate': 12524, 'type': 'auto', 'parkingspot': 'A12', 'duration': '12H', 'starttime': '12:00:03'})
    headers = {"Content-type": "application/x-www-form-urlencoded"}
    conn = httplib.HTTPConnection("131.155.238.86", "8085")
    conn.request("POST", "", params, headers)
    response = conn.getresponse()
    print("reservation for parkingspot " + str(name) + ", At date " + str(data) + " for " + str(duration) + " minutes succesfull!");
    print response.status, response.reason
    conn.close()

#POSTRequest();

Vehicle();