import wexpect
import time
import sys

_host = '192.168.56.2'
_username = 'user'
_pass = 'pass'
_port = 22

child = wexpect.spawn(f'ssh {_username}@{_host} -p {_port}', timeout=10, encoding='utf-8')

child.expect_exact('password',timeout=5)
child.sendline(_pass)

child.expect_exact('$', timeout=5)

print(child.before + child.after + child.buffer, flush=True)

child.sendline('sudo apt -y install aptitude')
print('sudo apt -y install aptitude')


def new_func(child):
    print('タイムアウト')
    child.expect_exact('$', timeout=10)
    print(child.before + child.after + child.buffer, flush=True)



index = child.expect_exact([r"password", r"$", wexpect.TIMEOUT], timeout=30)

if index == 0:
    print(child.before + child.after + child.buffer, flush=True)
    child.sendline(_pass)

    index2 = child.expect_exact([r"$", wexpect.TIMEOUT], timeout=30)
    if index2 == 1:
        new_func(child)
    else:
        print(child.before + child.after + child.buffer, flush=True)

elif index == 1:
    print(child.before + child.after + child.buffer, flush=True)

else:
     new_func(child)
        
     
child.sendline('exit')
child.close()
