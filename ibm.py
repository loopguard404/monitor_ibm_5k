#!/usr/bin/python3
 
import sys
import paramiko
import subprocess

target = 'ip'
login = 'user'
password = 'pass'
command = 'lssystem -delim \,'
 
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)
stdin, stdout, stderr = client.exec_command('lsdrive')
lsdrive = stdout.read()
lsdrive = lsdrive.decode('UTF-8')
file = '/etc/zabbix/scripts/ibm/result/10.0.0.180/lsdrive.txt'
with open(file, 'w') as file:
    file.write(lsdrive)


#stdin, stdout, stderr = client.exec_command('lssystemstats')
#lssystemstats = stdout.read()
#lssystemstats = lssystemstats.decode('UTF-8')
#file = '/etc/zabbix/scripts/ibm/result/10.0.0.180/lssystemstats.txt'
#with open(file, 'w') as file:
#    file.write(lssystemstats)


stdin, stdout, stderr = client.exec_command('lsarray')
lsarray = stdout.read()
lsarray = lsarray.decode('UTF-8')
file = '/etc/zabbix/scripts/ibm/result/10.0.0.180/lsarray.txt'
with open(file, 'w') as file:
    file.write(lsarray)


stdin, stdout, stderr = client.exec_command('lsenclosurebattery')
lsenclosurebattery = stdout.read()
lsenclosurebattery = lsenclosurebattery.decode('UTF-8')
file = '/etc/zabbix/scripts/ibm/result/10.0.0.180/lsenclosurebattery.txt'
with open(file, 'w') as file:
    file.write(lsenclosurebattery)


stdin, stdout, stderr = client.exec_command('lshost')
lshost = stdout.read()
lshost = lshost.decode('UTF-8')
file = '/etc/zabbix/scripts/ibm/result/10.0.0.180/lshost.txt'
with open(file, 'w') as file:
    file.write(lshost)



stdin, stdout, stderr = client.exec_command('lsnodecanisterstats')
lsnodecanisterstats = stdout.read()
lsnodecanisterstats = lsnodecanisterstats.decode('UTF-8')
file = '/etc/zabbix/scripts/ibm/result/10.0.0.180/lsnodecanisterstats.txt'
with open(file, 'w') as file:
    file.write(lsnodecanisterstats)


stdin, stdout, stderr = client.exec_command('lsmdiskgrp')
lsmdiskgrp = stdout.read()
lsmdiskgrp = lsmdiskgrp.decode('UTF-8')
file = '/etc/zabbix/scripts/ibm/result/10.0.0.180/lsmdiskgrp.txt'
with open(file, 'w') as file:
    file.write(lsmdiskgrp)



stdin, stdout, stderr = client.exec_command('lsportip')
lsportip = stdout.read()
lsportip = lsportip.decode('UTF-8')
file = '/etc/zabbix/scripts/ibm/result/10.0.0.180/lsportip.txt'
with open(file, 'w') as file:
    file.write(lsportip)


stdin, stdout, stderr = client.exec_command('lssevdiskcopy')
lssevdiskcopy = stdout.read()
lssevdiskcopy = lssevdiskcopy.decode('UTF-8')
file = '/etc/zabbix/scripts/ibm/result/10.0.0.180/lssevdiskcopy.txt'
with open(file, 'w') as file:
    file.write(lssevdiskcopy)


stdin, stdout, stderr = client.exec_command('lsvdisk')
lsvdisk = stdout.read()
lsvdisk = lsvdisk.decode('UTF-8')
file = '/etc/zabbix/scripts/ibm/result/10.0.0.180/lsvdisk.txt'
with open(file, 'w') as file:
    file.write(lsvdisk)


stdin, stdout, stderr = client.exec_command('lsvdiskanalysis')
lsvdiskanalysis = stdout.read()
lsvdiskanalysis = lsvdiskanalysis.decode('UTF-8')
file = '/etc/zabbix/scripts/ibm/result/10.0.0.180/lsvdiskanalysis.txt'
with open(file, 'w') as file:
    file.write(lsvdiskanalysis)
client.close()
