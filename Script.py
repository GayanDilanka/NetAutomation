from netmiko import ConnectHandler

#-------------Devices list-------------
R1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.200',
    'username': 'admin',
    'password': 'cisco12345'
}

R2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.2.2',
    'username': 'admin',
    'password': 'cisco12345'
}

R3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.4.2',
    'username': 'admin',
    'password': 'cisco12345'
}

R3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.77.1',
    'username': 'admin',
    'password': 'cisco12345'
}

devices_list = [R1,R2,R3,R4]

#-----------R1 Interfaces Configurations-------
net_connect = ConnectHandler(**R1)
print("Connected to R1")

print("Configuring Interfaces of R1")
config_commands = [
                    'interface serial 1/0',
                    'no shutdown'
                    'ip address 192.168.2.1 255.255.255.252',
                    'interface loopback 1',
                    'ip address 192.168.1.1 255.255.255.0',
                    'interface loopback 0',
                    'ip address 192.168.6.1 255.255.255.0'
                  ]
output = net_connect.send_config_set(config_commands)
print (output)

print("Configuring Clock Rate")
config_commands = [
                    'interface serial 1/0',
                    'clock rate 128000',
                  ]
output = net_connect.send_config_set(config_commands)
print (output)


print("Add ipv6 addresses")
config_commands = [
                    'interface serial 1/0'
                    'ipv6 address 2001:DB8:CAFE:2::1/64',
                    'ipv6 address FE80::1 link-local',
                  ]
output = net_connect.send_config_set(config_commands)
print (output)


print("****Configuring R1 Interfaces Completed*****")


#-----------R2 Interfaces Configurations-------

net_connect = ConnectHandler(**R2)
print("Connected to R2")

print("Configuring Interfaces of R2")
config_commands = [
                    'interface serial 1/0',
                    'no shutdown'
                    'ip address 192.168.2.2 255.255.255.252',
                    'interface serial 1/1',
                    'no shutdown',
                    'ip address 192.168.4.1 255.255.255.252',
                    'interface loopback 0',
                    'ip address 192.168.3.1 255.255.255.0'
                  ]
output = net_connect.send_config_set(config_commands)
print (output)

print("Configuring Clock Rate")
config_commands = [
                    'interface serial 1/0',
                    'clock rate 128000',
                  ]
output = net_connect.send_config_set(config_commands)
print (output)


print("Add ipv6 addresses")
config_commands = [
                    'interface serial 1/0',
                    'ipv6 address 2001:DB8:CAFE:2::1/64',
                    'ipv6 address FE80::1 link-local',
                    'interface serial 1/1',
                    'ipv6 address 2001:DB8:CAFE:4::1/64',
                    'ipv6 address FE80::2 link-local',
                    'interface loopback 0',
                    'ipv6 address 2001:DB8:CAFE:3::1/64',
                    'ipv6 address FE80::2 link-local',                    
                  ]
output = net_connect.send_config_set(config_commands)
print (output)


print("****Configuring R2 Interfaces Completed*****")


#-----------R3 Interfaces Configurations-------

net_connect = ConnectHandler(**R3)
print("Connected to R3")

print("Configuring Interfaces of R3")
config_commands = [
                    'interface serial 1/1',
                    'no shutdown'
                    'ip address 192.168.4.2 255.255.255.252',
                    'interface serial 1/2',
                    'no shutdown'
                    'ip address 192.168.77.2 255.255.255.252',
                    'interface loopback 0',
                    'ip address 192.168.5.1 255.255.255.0'
                  ]
output = net_connect.send_config_set(config_commands)
print (output)

print("Add ipv6 addresses")
config_commands = [
                    'interface serial 1/1',
                    'ipv6 address 2001:DB8:CAFE:4::2/64',
                    'ipv6 address FE80::3 link-local',
                    'interface serial 1/2  ',
                    'ipv6 address 2001:DB8:CAFE:77::2/64',
                    'ipv6 address FE80::3 link-local',
                    'interface loopback 0',
                    'ipv6 address 2001:DB8:CAFE:5::1/64',
                    'ipv6 address FE80::3 link-local',
                  ]
output = net_connect.send_config_set(config_commands)
print (output)


print("****Configuring R3 Interfaces Completed*****")



#-----------R4 Interfaces Configurations-------

net_connect = ConnectHandler(**R4)
print("Connected to R4")

print("Configuring Interfaces of R4")
config_commands = [
                    'interface serial 1/2',
                    'no shutdown'
                    'ip address 192.168.77.1 255.255.255.252',
                    'interface loopback 0',
                    'ip address 192.168.99.1 255.255.255.0'
                  ]
output = net_connect.send_config_set(config_commands)
print (output)

print("Add ipv6 addresses")
config_commands = [
                    'interface serial 1/2',
                    'ipv6 address 2001:DB8:CAFE:77::1/64',
                    'ipv6 address FE80::4 link-local',
                    'interface loopback 0',
                    'ipv6 address 2001:DB8:CAFE:77::2/64',
                    'ipv6 address FE80::4 link-local',
                  ]
output = net_connect.send_config_set(config_commands)
print (output)


print("****Configuring R4 Interfaces Completed*****")




#-------------OSPF CONFIGURATION------

print("Configuring IPV4 OSPF on R2")
net_connect = ConnectHandler(**R2)
print("Connected to R2")

config_commands = [
                    'router ospf 1',
                    'router-id 2.2.2.2',
                    'network 192.168.2.0 0.0.0.255 area 0',
                    'network 192.168.4.0 0.0.0.255 area 0',
                    'network 192.168.3.0 0.0.0.255 area 0'
                  ]
output = net_connect.send_config_set(config_commands)
print (output)

print("Configuring IPV4 OSPF on R3")
net_connect = ConnectHandler(**R3)
print("Connected to R3")

config_commands = [
                    'router ospf 1',
                    'router-id 3.3.3.3',
                    'network 192.168.5.0 0.0.0.255 area 0',
                    'network 192.168.4.0 0.0.0.255 area 0',
                    'network 192.168.77.0 0.0.0.255 area 0'
                  ]
output = net_connect.send_config_set(config_commands)
print (output)


print("****Configuring IPV4 OSPF Completed*****")

#****IPV6 OSPF*********


print("Configuring IPV6 OSPF on R2")
net_connect = ConnectHandler(**R2)
print("Connected to R2")

config_commands = [
                    'router ospf 1',
                    'router-id 2.2.2.2',
                    'exit',
                    'interface serial 1/1',
                    'ipv6 ospf 1 area 0'
                    'interface loopback 0',
                    'ipv6 ospf 1 area 0'                    
                  ]
output = net_connect.send_config_set(config_commands)
print (output)

print("Configuring IPV6 OSPF on R3")
net_connect = ConnectHandler(**R3)
print("Connected to R3")

config_commands = [
                    'router ospf 1',
                    'router-id 3.3.3.3',
                    'exit',
                    'interface serial 1/1',
                    'ipv6 ospf 1 area 0'
                    'interface loopback 0',
                    'ipv6 ospf 1 area 0'                    
                  ]
output = net_connect.send_config_set(config_commands)
print (output)


print("****Configuring IPV6 OSPF Completed*****")



#------------EIGRP configuration-----

print("Configuring IPV4 EIGRP on R1")
net_connect = ConnectHandler(**R1)
print("Connected to R1")

config_commands = [
                    'router eigrp 65000',
                    'network 192.168.2.0 0.0.0.255',
                    'network 192.168.1.0 0.0.0.255',
                    'network 192.168.6.0 0.0.0.255',
                    'no auto-summary '                 
                  ]
output = net_connect.send_config_set(config_commands)
print (output)

print("Configuring IPV4 EIGRP on R2")
net_connect = ConnectHandler(**R2)
print("Connected to R2")

config_commands = [
                    'router eigrp 65000',
                    'network 192.168.2.0 0.0.0.255',
                    'network 192.168.3.0 0.0.0.255',
                    'network 192.168.4.0 0.0.0.255',
                    'no auto-summary '                 
                  ]
output = net_connect.send_config_set(config_commands)
print (output)



print("Configuring IPV6 EIGRP on R1")
net_connect = ConnectHandler(**R1)
print("Connected to R1")

config_commands = [
                    'ipv6 router eigrp 65000',  
                    'exit'
                    'interface serial 1/0', 
                    'ipv6 eigrp 65000'          
                  ]
output = net_connect.send_config_set(config_commands)
print (output)


print("Configuring IPV6 EIGRP on R2")
net_connect = ConnectHandler(**R2)
print("Connected to R2")

config_commands = [
                    'ipv6 router eigrp 65000',  
                    'exit',
                    'interface serial 1/0'  ,
                    'ipv6 eigrp 65000',        
                  ]
output = net_connect.send_config_set(config_commands)
print (output)

print("****Configuring EIGRP Completed*****")


#--------Redistribution between OSPF and EIGRP------

print("Configuring Redistributionon R2")
net_connect = ConnectHandler(**R2)
print("Connected to R2")

config_commands = [
                    'router ospf 1',  
                    'redistribute eigrp 65000 subnets ',
                    'interface serial 1/0',  
                    'exit',
                    'router eigrp 65000',
                    'redistribute ospf 1 metric 10000 100 255 1 1500 ', 
                    'ipv6 router ospf 1',
                    'redistribute eigrp 65000',
                    'router eigrp 65000',
                    'redistribute ospf 1 metric 10000 100 255 1 1500 ',

                  ]
output = net_connect.send_config_set(config_commands)
print (output)



#-------Change Hello and Dead Timers------

print("Configuring Hello and Dead Timers R2")
net_connect = ConnectHandler(**R2)
print("Connected to R2")

config_commands = [
                    'interface serial 1/1',  
                    'ip ospf hello-interval 10',
                    'ip ospf dead-interval 30'                  ]
output = net_connect.send_config_set(config_commands)
print (output)



print("Configuring Hello and Dead Timers  R3")
net_connect = ConnectHandler(**R3)
print("Connected to R3")

config_commands = [
                    'interface serial 1/1',  
                    'ip ospf hello-interval 10',
                    'ip ospf dead-interval 30'  
                  ]
output = net_connect.send_config_set(config_commands)
print (output)



#-------------Apply secure interface authentication between R2 & R3 for OSPF --------


print("Configuring interface authentication  R2")
net_connect = ConnectHandler(**R2)
print("Connected to R2")

config_commands = [
                    'interface serial 1/1',  
                    'ip ospf hello-interval 10',
                    'ip ospf dead-interval 30'  
                  ]
output = net_connect.send_config_set(config_commands)
print (output)



print("Configuring interface authentication   R3")
net_connect = ConnectHandler(**R2)
print("Connected to R2")


config_commands = [
                    'interface serial 1/1',  
                    'ip ospf hello-interval 10',
                    'ip ospf dead-interval 30'  
                  ]

output = net_connect.send_config_set(config_commands)
print (output)




print ("************OSPF authentication configuration completed")



#---------Configure BGP Peering--------------


print("Configuring BGP Peering  R3")
net_connect = ConnectHandler(**R3)
print("Connected to R3")

config_commands = [
                    'router bgp 65000',  
                    'neighbor 192.168.77.1 remote-as 65100 ',
                    'network 192.168.5.0 mask 255.255.255.0',
                    'network 192.168.4.0 mask 255.255.255.252' 
                  ]
output = net_connect.send_config_set(config_commands)
print (output)



print("Configuring interface authentication   R4")
net_connect = ConnectHandler(**R4)
print("Connected to R4")


config_commands = [
                    'router bgp 65100',  
                    'neighbor 192.168.77.2 remote-as 65000',
                    'network 192.168.99.0 mask 255.255.255.0'  
                  ]

output = net_connect.send_config_set(config_commands)
print (output)

print ("***********BGP Peering configuration completed")



#---------Infecting Deafult route to  BGP --------------


print("Configuring BGP Peering  R4")
net_connect = ConnectHandler(**R4)
print("Connected to R4")

config_commands = [
                    'ip route 0.0.0.0 0.0.0.0 serial 1/2',
                    'router bgp 65100',
                    'redistribute Connected subnets',  
                  ]
output = net_connect.send_config_set(config_commands)
print (output)



#---Filter the 192.168.6.0/24 network from entering the OSPF routing domain


print("Filter OSPF  Traffic")
net_connect = ConnectHandler(**R1)
print("Connected to R1")

config_commands = [
                    'ip access-list standard deny_6_0',
                    'deny 192.168.6.0 0.0.0.255',
                    'router ospf 1',  
                    'distribute-list deny_6_0 in'
                  ]
output = net_connect.send_config_set(config_commands)
print (output)



#---Configure R4 as an NTP server


print("Configuring BGP Peering  R4")
net_connect = ConnectHandler(**R4)
print("Connected to R4")

config_commands = [
                    'ntp master 1',
                  ]
output = net_connect.send_config_set(config_commands)
print (output)



#---------Creating Local Authentication----

for device in devices_list:
    net_connect = ConnectHandler(**device)
    print("Connected to"+ device)
    config_commands = [
                    'ip domain-name cisco.com',
                    'crypto key generate rsa',
                    '1024',
                    'ip ssh version 2',
                    'username admin password cisco12345',
                    'line vty 0 4',
                    'login local',
                    'transport input ssh'

                  ]
    output = net_connect.send_config_set(config_commands)
    print (output)


print("Authentication Configuring Completed")

#--------Checks from R1--------------
net_connect = ConnectHandler(**R1)
print("Connected to R1")
#output = net_connect.send_command('show ip int brief')
print("Checking Connectivity to R2")
output= net_connect.send_command('ping 192.168.2.2')
last_line = str(output.splitlines()[-1:][0])
words_list = last_line.split()
#print(words_list[3])
if int(words_list[3]) > 0 :
    print("Connection Sucees")
else:
    print("Connection Faliled")

print("Checking Connectivity to R3")
output= net_connect.send_command('ping 192.168.4.2')
last_line = str(output.splitlines()[-1:][0])
words_list = last_line.split()
#print(words_list[3])
if int(words_list[3]) > 0 :
    print("Connection Sucees")
else:
    print("Connection Faliled")

print("Checking Connectivity to R4")
output= net_connect.send_command('ping 192.168.77.1')
last_line = str(output.splitlines()[-1:][0])
words_list = last_line.split()
#print(words_list[3])
if int(words_list[3]) > 0 :
    print("Connection Sucees")
else:
    print("Connection Faliled")

print("Connectivity tests from R1 Completed")


#-------------R1 checks completed-----------


#--------Checks from R2--------------
net_connect = ConnectHandler(**R2)
print("Connected to R2")
#output = net_connect.send_command('show ip int brief')
print("Checking Connectivity to R1")
output= net_connect.send_command('ping 192.168.2.1')
last_line = str(output.splitlines()[-1:][0])
words_list = last_line.split()
#print(words_list[3])
if int(words_list[3]) > 0 :
    print("Connection Sucees")
else:
    print("Connection Faliled")

print("Checking Connectivity to R3")
output= net_connect.send_command('ping 192.168.4.2')
last_line = str(output.splitlines()[-1:][0])
words_list = last_line.split()
#print(words_list[3])
if int(words_list[3]) > 0 :
    print("Connection Sucees")
else:
    print("Connection Faliled")

print("Checking Connectivity to R4")
output= net_connect.send_command('ping 192.168.77.1')
last_line = str(output.splitlines()[-1:][0])
words_list = last_line.split()
#print(words_list[3])
if int(words_list[3]) > 0 :
    print("Connection Sucees")
else:
    print("Connection Faliled")

print("Connectivity tests from R2 Completed")


#-------------R2 checks completed-----------

#--------Checks from R2--------------
net_connect = ConnectHandler(**R2)
print("Connected to R2")
#output = net_connect.send_command('show ip int brief')
print("Checking Connectivity to R1")
output= net_connect.send_command('ping 192.168.2.1')
last_line = str(output.splitlines()[-1:][0])
words_list = last_line.split()
#print(words_list[3])
if int(words_list[3]) > 0 :
    print("Connection Sucees")
else:
    print("Connection Faliled")

print("Checking Connectivity to R3")
output= net_connect.send_command('ping 192.168.4.2')
last_line = str(output.splitlines()[-1:][0])
words_list = last_line.split()
#print(words_list[3])
if int(words_list[3]) > 0 :
    print("Connection Sucees")
else:
    print("Connection Faliled")

print("Checking Connectivity to R4")
output= net_connect.send_command('ping 192.168.77.1')
last_line = str(output.splitlines()[-1:][0])
words_list = last_line.split()
#print(words_list[3])
if int(words_list[3]) > 0 :
    print("Connection Sucees")
else:
    print("Connection Faliled")

print("Connectivity tests from R2 Completed")


#-------------R2 checks completed-----------

#--------Checks from R3--------------
net_connect = ConnectHandler(**R3)
print("Connected to R3")
#output = net_connect.send_command('show ip int brief')
print("Checking Connectivity to R1")
output= net_connect.send_command('ping 192.168.2.1')
last_line = str(output.splitlines()[-1:][0])
words_list = last_line.split()
#print(words_list[3])
if int(words_list[3]) > 0 :
    print("Connection Sucees")
else:
    print("Connection Faliled")

print("Checking Connectivity to R2")
output= net_connect.send_command('ping 192.168.4.1')
last_line = str(output.splitlines()[-1:][0])
words_list = last_line.split()
#print(words_list[3])
if int(words_list[3]) > 0 :
    print("Connection Sucees")
else:
    print("Connection Faliled")

print("Checking Connectivity to R4")
output= net_connect.send_command('ping 192.168.77.1')
last_line = str(output.splitlines()[-1:][0])
words_list = last_line.split()
#print(words_list[3])
if int(words_list[3]) > 0 :
    print("Connection Sucees")
else:
    print("Connection Faliled")

print("Connectivity tests from R3 Completed")


#-------------R3 checks completed-----------


#--------Checks from R3--------------
net_connect = ConnectHandler(**R3)
print("Connected to R3")
#output = net_connect.send_command('show ip int brief')
print("Checking Connectivity to R1")
output= net_connect.send_command('ping 192.168.2.1')
last_line = str(output.splitlines()[-1:][0])
words_list = last_line.split()
#print(words_list[3])
if int(words_list[3]) > 0 :
    print("Connection Sucees")
else:
    print("Connection Faliled")

print("Checking Connectivity to R2")
output= net_connect.send_command('ping 192.168.4.1')
last_line = str(output.splitlines()[-1:][0])
words_list = last_line.split()
#print(words_list[3])
if int(words_list[3]) > 0 :
    print("Connection Sucees")
else:
    print("Connection Faliled")

print("Checking Connectivity to R4")
output= net_connect.send_command('ping 192.168.77.1')
last_line = str(output.splitlines()[-1:][0])
words_list = last_line.split()
#print(words_list[3])
if int(words_list[3]) > 0 :
    print("Connection Sucees")
else:
    print("Connection Faliled")

print("Connectivity tests from R3 Completed")


#-------------R3 checks completed-----------

#--------Checks from R4--------------
net_connect = ConnectHandler(**R4)
print("Connected to R4")
#output = net_connect.send_command('show ip int brief')
print("Checking Connectivity to R1")
output= net_connect.send_command('ping 192.168.2.1')
last_line = str(output.splitlines()[-1:][0])
words_list = last_line.split()
#print(words_list[3])
if int(words_list[3]) > 0 :
    print("Connection Sucees")
else:
    print("Connection Faliled")

print("Checking Connectivity to R2")
output= net_connect.send_command('ping 192.168.4.1')
last_line = str(output.splitlines()[-1:][0])
words_list = last_line.split()
#print(words_list[3])
if int(words_list[3]) > 0 :
    print("Connection Sucees")
else:
    print("Connection Faliled")

print("Checking Connectivity to R3")
output= net_connect.send_command('ping 192.168.77.2')
last_line = str(output.splitlines()[-1:][0])
words_list = last_line.split()
#print(words_list[3])
if int(words_list[3]) > 0 :
    print("Connection Sucees")
else:
    print("Connection Faliled")

print("Connectivity tests from R4 Completed")


#-------------R4 checks completed-----------