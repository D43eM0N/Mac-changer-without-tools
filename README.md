# MAC Address Changer

A lightweight command-line tool written in Python that changes the MAC address of network interfaces on Linux systems using low-level sockets and ioctl system calls.

Requirements:

- Linux Operating System (Required due to low-level system calls and SIOCSIFHWADDR).

- Python 3

-  Root (Administrator) Privileges

Installation:
1.Clone or download the repository:
```Bash
git clone https://github.com/D43eM0N/Mac-changer-without-tools.git
cd Mac-changer-without-tools
```
    2.Install the required Python library:
    ```Bash
        pip install getmac
    ```
Usage:

The script requires the new MAC address and the target network interface as arguments. Because it performs system-level modifications, it must be run with sudo:
Bash

    `sudo python3 mac_changer.py <new_mac_address> <network_interface>`

Example:
     `sudo python3 mac_changer.py 00:11:22:33:44:55 eth0`
