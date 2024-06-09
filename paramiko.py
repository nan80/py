import paramiko

_host = '192.168.56.2'
_username = 'user'
_pass = 'pass'

list_of_commands = ["which ssh", "date", "whoami", ]

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(_host, username=_username, password=_pass)

stdin, stdout, stderr = ssh.exec_command('ls')
print(stdout.read().decode())

for c in list_of_commands:
    print("Command:", c)
    stdin, stdout, stderr = ssh.exec_command(c)
    print("Output:\n", stdout.read().decode())
    
ssh.close()
