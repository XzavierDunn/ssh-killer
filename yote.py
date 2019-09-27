import os
from paramiko import SSHClient, RSAKey, AutoAddPolicy

port = input('port: ')
hostname = input('Hostname/ip: ')
username = input('Username: ')
pwd = input('Password (if you need it): ')

os.system(f'scp yeet.sh {username}@{hostname}:~/')

ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect(hostname, port, username, pwd)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('sudo +x chmod yeet.sh')
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('./yeet.sh')
print(ssh_stdout)

ssh.close()
