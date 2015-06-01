a=raw_input()
b=raw_input()
c=[]
for i in range(len(a)):
	x=int(a[i],16)^int(b[i%len(b)],16)
	c.append('{:x}'.format(x))
print ''.join(c)
