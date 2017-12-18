# DHL attack
Delivery attack to DHL tracking system.


DHL use a random generated 6 alphanumeric chars to index and notify the shipment.
There is no captcha and no authentication methods.


The system can be attack with a bruteforce of the 6 alphanumeric chars code and can be hidden using a botnet or tor proxies.

### Sources:
* dhlattack.py: make a single random attack
* start.sh: run multi requests in parallel

### Twitter info message
* https://twitter.com/0xVaccaro/status/942690762613035008
