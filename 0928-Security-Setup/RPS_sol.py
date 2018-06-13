from pwn import *

r = remote('bamboofox.cs.nctu.edu.tw', 22004)

# 0:rock 1:paper 2:scissors
catch = {'!':0, '?':1, ':':2}
output = ['rock', 'paper', 'scissors']
r.recvuntil('game')
mark = r.recvuntil('\n')[0]
current = (catch[mark] + 1) % 3
for i in xrange(100):
	r.recvuntil(':')
	r.sendline(output[current])
	current = (current + 1) % 3

r.interactive()
