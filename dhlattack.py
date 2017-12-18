#!/usr/bin/python
import requests 
import random


def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session
    
session = get_tor_session()

id = ''.join(random.choice('0123456789qwertyuiopasdfghjklzxcvbnm') for i in range(6))
r = session.get("http://delivery.dhl.com/IT/"+id)
text = r.text.encode('utf-8')

if text.find("for latest shipment status".encode()) != -1 :
	print ("http://delivery.dhl.com/IT/"+id)