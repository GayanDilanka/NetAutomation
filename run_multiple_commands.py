
from netmiko import ConnectHandler

with open('commands_file') as f:
	commands_to_send = f.read().splitlines()

	print(commands_to_send)
	print(commands_to_send[0])
	iosv_l2_s1 = {
	    'device_type': 'cisco_ios',
	    'ip': '192.168.122.72',
	    'username': 'gayan',
	    'password': 'cisco',
	}

	net_connect = ConnectHandler(**iosv_l2_s1)
	net_connect.enable()
	output = net_connect.send_config_set(commands_to_send)
	print(output)
