import netmiko

from device_list import device_list
from users import users

device_type = ''
username = ''
password = ''

for x in device_list:
	connection = netmiko.ConnectHandler(ip=x, device_type=device_type, username=username, password=password)
	print("\nConnected to: ", x)
	for z in users:
		print(connection.send_command(z, delay_factor=15))
	connection.disconnect()