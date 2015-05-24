from operator import xor
s1=raw_input("String 1:")

s2=raw_input("String 2:")
s3=[]
s1=list(s1)
s2=list(s2)
#print len(s1)
if len(s1)!=len(s2):
	print "Abort!!"
else:
	for i in range(len(s1)):
		s3.append(chr(ord(s1[i])^ord(s2[i])))
	print ''.join(s3)
