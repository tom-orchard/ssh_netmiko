# Readme.

This is a very basic Netmiko script that allows a user to put in a list of SSH manageable devices and send commands via a loop.

There are three configurable variables that can be precoded.
1. 'device_type'
2. 'username'
3. 'password'

The device list can be found in the [Netmiko Github](https://github.com/ktbyers/netmiko) list of supported devices, as well as some commands that can be run.

The use case I had for this script is to add a user and accprofile on a range of managed Fortinet Firewalls. As this script is very basic (and because I'm still a beginner), this script fails under a few conditions:
1. the device is split into vdoms
2. the device username/password is something different to what is precoded
3. a device hangs for more than 15 seconds (which usually means it is unreachable)

To run the script, do the following:
(ideally) run in a venv
(pre-req) pip install netmiko
1. hardcode device_type, username, password
2. add the hostname/IP to the array inside the device_list.py file
3. add the commands inside the users.py file. An example of this is done already, the array contains the commands, there is then a .join to allow it to be added as an argument.

Enjoy.


