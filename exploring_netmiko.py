#!/usr/bin/env python

from netmiko import ConnectHandler

HOST = "10.254.0.1"  # Host name
USER = "cisco"  # Username to access the router
PASS = "cisco"  # Password for authentication
TYPE = "cisco_xe"  # Device type

# Using Netmiko's ConnectHandler class initiate a connection to the device
r1 = ConnectHandler(host=HOST, username=USER, password=PASS, device_type=TYPE)
