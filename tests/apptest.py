#!/usr/bin/env python3
"""
Tests App connection
"""
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

import sys
sys.path.append('../')

def testconnection(hostname,port):
    url = 'http://' + hostname + ':' + port

    with requests.Session() as session:
        retries = Retry(
            total=10,
            backoff_factor=0.2,
            status_forcelist=[500,502,503,504])
    
    print (f"Connecting to container.....{url}")
    try:
        session.mount('http://', HTTPAdapter(max_retries=retries))
        r = session.get(url)
        print(r.text)
        return r.status_code
    except requests.exceptions.RequestException as error:
        raise SystemExit(error)
   
if __name__ == '__main__':
    hostname = input('Input hostname: ')
    port     = input('Input port number of app: ')

    testconnection(hostname,port)


    
