import httplib, urllib


def GETRequest():
    conn = httplib.HTTPConnection("www.python.org")
    conn.request("GET", "/index.html")
    r1 = conn.getresponse()
    print r1.status, r1.reason
    conn.close()

def POSTRequest():
    params = urllib.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
    headers = {"Content-type": "application/x-www-form-urlencoded",
                ...            "Accept": "text/plain"}
    conn = httplib.HTTPConnection("bugs.python.org")
    conn.request("POST", "", params, headers)
    response = conn.getresponse()
    print response.status, response.reason
    conn.close()