#!/bin/python3
import requests, secrets
from requests.auth import HTTPBasicAuth
import xml.etree.ElementTree as ET

#https://webservices.iso-ne.com/api/v1.1/fiveminutesystemload/current

sysLoadFiveMinCurrent = "/fiveminutesystemload/current"

username = secrets.username
password = secrets.password

queryURL = f"{secrets.rootUrl}{sysLoadFiveMinCurrent}"

print(f"Trying URL: {queryURL} with using U: {username} & P: {password}")
response = requests.get(queryURL, auth=HTTPBasicAuth(username, password))
print(response.status_code)
if response.status_code == 200:
    namespace = {'ns': 'http://WEBSERV.iso-ne.com'}
    print(namespace)
    root = ET.fromstring(response.content)
    print(root)
    load_mw = root.find("ns:LoadMw", namespace).text
    print(f"Load MW: {load_mw}")

else:
    print(f"API Call failed with: {response.status_code}")