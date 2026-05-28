#!usr/bin/env python

from netmiko import ConnectHandler

HOST = "10.254.0.1"  # Host name
USER = "cisco"  # Username
PASS = "cisco"  # Password for authentication
TYPE = "cisco_xe"  # Device type

device = ConnectHandler(
    host=HOST, username=USER, password=PASS, device_type=TYPE
)

router = "r1"
print("Connecting to {}".format(router))

print("Sending SNMP Configurations to {}...".format(router))

file_path = "./configs/{}.cfg".format(router)
device.send_config_from_file(file_path)
print("Commands sent to device...")

print("Verifying Configuration {}...".format(router))

snmp_config = device.send_command(
    "show run | include snmp-server"
)
print(snmp_config)
print("Disconnecting from {}...".format(router))

#Connecting to r1
#Sending SNMP Configurations to r1...
#Commands sent to device...
#Verifying Configuration r1...
#snmp-server community public RO
#snmp-server community private RW
#snmp-server community cisco-devnet RO
#snmp-server community cisco-secure RW
#snmp-server location california
#snmp-server contact cisco_lab
#Disconnecting from r1...
