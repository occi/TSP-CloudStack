print('testing writing into a log file')
f=open('content.log','r')
r=f.readlines()
print 'cont',r
f.close()

f=open('content.log','w')
f.write('')


f.close()

print 'end'
print file('content.log').read()
