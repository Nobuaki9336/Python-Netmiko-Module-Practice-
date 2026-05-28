# Cisco Network Automation with Netmiko

This repository demonstrates how to transition from traditional CLI networking to **NetDevOps / Network Automation** using the Python `netmiko` library. It contains a collection of scripts that progress from a simple connection test to dynamic multi-device configuration deployments.

## Network Topology

The scripts are developed and tested against the following multi-router Cisco CSR1000v lab topology managed via a Linux Student Workstation:

<img src="net_topology_github.png" alt="Network Topology" width="900">

---

## Prerequisites & Installation

Before running the scripts, ensure you have Python installed and the Netmiko module initialized:

```bash
pip install netmiko
```
Automation Scripts Overview

The repository structures the learning curve into 4 progressive automation stages:

1. Basic Connectivity Test (exploring_netmiko.py)

The foundational script used to verify network reachability and SSH authentication parameters.
Core Function: Uses Netmiko's ConnectHandler class to initiate a secure SSH session to a single target device (cisco_xe).
Use Case: Verifies that raw management network paths (TCP Port 22) and credentials are functioning correctly before pushing changes.

2. File-Based Configuration Deployment (single_device_config.py)

Advances from simple connectivity to pushing specific configuration blocks from external files and capturing immediate verification data.

Key Mechanisms:
send_config_from_file(): Reads Cisco CLI commands line-by-line from an external file (./configs/r1.cfg) and deploys them atomically.
send_command(): Executes show run | include snmp-server to programmatically parse and verify that the target configurations were correctly running in the running-config.

3. Loop-Driven Multi-Device Configurations (multiple_device_config.py)

Demonstrates scalability by introducing a Python Dictionary (inventory) acting as a lightweight Source of Truth to programmatically target multiple nodes sequentially.

Core Function: Iterates through r1, r2, and r3 metadata using a python for router, detail in inventory.items(): loop, standardizing configurations globally without manual intervention.

4. Dynamic Data Modeling & Command Construction (construct_script.py)

The most mature stage of the automation pipeline, decoupling infrastructure definitions from runtime deployment values.

Advanced Concepts:
Data Decoupling: Separates static access credentials (inventory) from dynamic desired network states (ip_info dict containing specific Loopback and Subnet Mask definitions).
String Templates: Uses format strings such as "interface {}" and "ip address {} {}" to dynamically render runtime variables into precise Cisco IOS-XE syntax.
send_config_set(): Batches the programmatically generated commands into individual transactional execution blocks per device.

Sample Execution Output
Below is the verified terminal logging output when executing single_device_config.py to deploy SNMP settings:

Connecting to r1
Sending SNMP Configurations to r1...
Commands sent to device...
Verifying Configuration r1...
snmp-server community public RO
snmp-server community private RW
snmp-server community cisco-devnet RO
snmp-server community cisco-secure RW
snmp-server location california
snmp-server contact cisco_lab
Disconnecting from r1...

