from pwn import *

#0:rock 1:paper 2:scissors
play = {'!':0, '?':1, ':':2}
sign = ['rock', 'paper', 'scissors']

r = remote('bamboofox.cs.nctu.edu.tw', 22004)
r.recvuntil('game')
mark = r.recvuntil('\n')[0]

current = (play[mark] + 1) % 3

for i in xrange(100):
	r.recvuntil(':')
	r.sendline(sign[current])
	current = (current + 1) % 3

r.interactive()
