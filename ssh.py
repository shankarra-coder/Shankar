'''
This script will allow you to ssh into unix based systems and allow you to run some commands

prerequisites for connecting to remote server:
- sshd service should be up and running on remote server.
- password authentication is YES in sshd_config file.
- get username,Password and hostname or remote server.

'''


import paramiko

user = 'root'
passwd = 'Vmware1!'
ip_address = "1.2.3.4"

# Creating an instance of SSHClient from paramiko module.
ssh = paramiko.SSHClient()

# Adding Fingerprint Automatically to know list
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

# Connecting to remote server and establish connectivity
ssh.connect(hostname=ip_address, username=user, password=passwd)
print('SSH Connection established successfully...')

# To execute some command on remote server
print('Please wait, Executing command on Remote server ...')
stdin,stdout,stderr = ssh.exec_command('date')
stdout = stdout.readline()   #Reading output using stdout.readline()
print(stdout)

cmd = 'vmware -vl'
stdin,stdout,stderr = ssh.exec_command(cmd)
stdout = stdout.readline()   #Reading output using stdout.readline()
print(stdout)



