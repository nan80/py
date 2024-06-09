#wexpectを使ったSSHログイン＋対話型コマンド実行例

import wexpect
import time
import sys

_host = '192.168.56.2'
_username = 'user'
_pass = 'pass'
_port = 22

butt = "vlc"

# Create an instance to execute the command
child = wexpect.spawn(f'ssh {_username}@{_host} -p {_port}', timeout=10, encoding='utf-8')

# Wait for a specific word
child.expect_exact('password',timeout=5)

# Send command
child.sendline(_pass)

child.expect_exact('$', timeout=5)

# Output Progress
print(child.before + child.after + child.buffer, flush=True)

child.sendline('ls')
child.expect_exact('$', timeout=5)
print(child.before + child.after + child.buffer, flush=True)

child.sendline('sudo whoami')
print('sudo whoami')
child.expect_exact('password', timeout=5)

child.sendline(_pass)
child.expect_exact('$', timeout=5)
print(child.before + child.after + child.buffer, flush=True)

child.sendline('exit')
