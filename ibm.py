#!/usr/bin/python3
 
import paramiko
 
target = 'ip'
login = 'user'
password = 'pass'
command = 'lssystem -delim \,'
 
def ssh_exec(command, target, user, password, port=22):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 
    try:
        client.connect(target, username=user, password=password, port=port)
    except:
        print('FATAL: Unable to log in')
        exit(1)
 
    stdin, stdout, stderr = client.exec_command(command)
 
    error = stderr.read()
    if error:
        error = error.decode('US-ASCII')
        print('Error running the command:{}'.format(error))
        client.close()
        return 0
 
    data = stdout.read()
    client.close()
 
    return data.decode('US-ASCII')
 
lssystem = ssh_exec(command, target, login, password)
print(lssystem)
