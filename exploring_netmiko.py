#!/usr/bin/env python

from netmiko import ConnectHandler

HOST = "10.254.0.1"  # Host name
USER = "cisco"  # Username to access the router
PASS = "cisco"  # Password for authentication
TYPE = "cisco_xe"  # Device type

# Using Netmiko's ConnectHandler class initiate a connection to the device
r1 = ConnectHandler(host=HOST, username=USER, password=PASS, device_type=TYPE)


r1.is_alive()
r1.disconnect()
r1.is_alive()
r1.establish_connection()
r1.is_alive()
r1.open_session_log("r1_session_logs.log")
r1.send_command("terminal length 0")
r1.send_command("show version")
commands = ['interface GigabitEthernet1', 'description DESCRIPTION WAS CHANGED VIA PYTHON']
r.send_config_set(commands)
r1.send_command("show interface GigabitEthernet1 description")
r1.disconnect()
exit()




