from pwn import *

r = remote('bamboofox.cs.nctu.edu.tw', 22005)

r.recvuntil('(')
low = int(r.recvuntil('~ ')[0])
high = int(r.recvuntil('=')[:9])
print (low,high)
while True:	
	output = (low + high) / 2
	print output 
	r.sendline(str(output))
	get = r.recvuntil('\n')
	if 'small' in get:
		low = output + 1
	elif 'big' in get:
		high = output - 1
	else:	
		print 'The answer is:', output		
		break

r.interactive()
