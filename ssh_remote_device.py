'''
This script will allow you to SSH into a remote device and perform basic actions
'''

import  paramiko
import time
esx_commands = [
                'date',
                'vmware -vl',
                'esxcfg-nics -l'
                ]

def ssh_remote_device():
    address = input("IP address : ")
    u_name = input("Username : ")
    pass_wd = input("Password : ")

    sshclient = paramiko.SSHClient()
    sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    sshclient.connect(username=u_name, password=pass_wd, hostname=address)

    for command in esx_commands:
        print(command)
        stdin, stdout, stderr = sshclient.exec_command(command)
        stdout = stdout.readlines()  # Reading output using stdout.readline()
        print(stdout)
        time.sleep(3)

    sshclient.close()

ssh_remote_device()