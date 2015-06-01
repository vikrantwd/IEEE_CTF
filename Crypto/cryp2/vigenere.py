p=raw_input().upper()
k=raw_input().upper()
c=[]
for i in range(len(p)):
	x=ord(p[i])+ord(k[i%len(k)])-65
	if x<=90:
		c.append(chr(x))
	else:
		c.append(chr(x-90+64))
print "".join(c)
