#!/usr/bin/python3


import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print("Usage:  " + sys.argv[0] + "<url>")
    sys.exit(1)
    
rq = requests.get("http://" + sys.argv[1])

if rq.status_code == 200:
   print("Success")

print("\n"+str(rq.headers)) 
   
gethostby_ = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of "+sys.argv[1]+" is: "+gethostby_ + "\n")

req_two = requests.get("https://ipinfo.io/"+gethostby_+"/json")
resp_ = json.loads(req_two.text)

print("Location: "+resp_["loc"])
print("Region: "+resp_["region"])
print("City: "+resp_["city"])
print("Country: "+resp_["country"])
print("give me a bottle of rum!")
