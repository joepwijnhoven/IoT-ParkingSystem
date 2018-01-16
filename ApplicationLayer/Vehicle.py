import httplib, urllib


def GETRequest():
    import httplib
    conn = httplib.HTTPConnection("192.168.178.24", "8085")
    conn.request("GET", "/parkingspotsAvailable")
    res = conn.getresponse()
    print res.status, res.reason

def POSTRequest():
    params = urllib.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
    headers = {"Content-type": "application/x-www-form-urlencoded"}
    conn = httplib.HTTPConnection("bugs.python.org")
    conn.request("POST", "", params, headers)
    response = conn.getresponse()
    print response.status, response.reason
    conn.close()

GETRequest();