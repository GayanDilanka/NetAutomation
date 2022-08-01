
from netmiko import ConnectHandler
from getpass import getpass
username = input("Enter the Username: ")
password = getpass()

with open('commands_file') as f:
	commands_to_send = f.read().splitlines()

with open('devices_file') as f:
	devices_list = f.read().splitlines()


print(commands_to_send)
print(devices_list)


for device in devices_list:
	print("Connecting to Device" + device)
	ip_address = device

	iosv_l2_s1 = {
	    'device_type': 'cisco_ios',
	    'ip': ip_address,
	    'username': username,
	    'password': password,
	}

	net_connect = ConnectHandler(**iosv_l2_s1)
	output = net_connect.send_config_set(commands_to_send)
	print(output)

