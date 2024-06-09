import paramiko

_host = '192.168.56.2'
_username = 'user'
_pass = 'pass'
_port = 22


list_of_commands = ["which ssh", "date", "whoami", ]

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(_host, username =_username, password =_pass, port = _port)

cmd = "sudo apt -y install aptitude"
print("Command:", cmd)
stdin, stdout, stderr = ssh.exec_command(cmd, get_pty=True)

while len(stdout.channel.in_buffer) == 0:
    # stdoutにパスプロンプトが出力されるまで待ち続ける
    continue

# 反応が悪いホストの場合は入力可能になるまで待った方がいい？
# time.sleep(1)

# sudoパスワード入力
print("Pass:", _pass)
stdin.channel.send(_pass + "\n")

# stdinだけ閉じる
stdin.channel.shutdown_write()

# 実行結果
print(stdout.read().decode().strip())

ssh.close()
