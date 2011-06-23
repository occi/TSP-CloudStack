
######### pour savoir l'id et l'ip de la vm creee
print 'testing result of creating'
ch='<COMPUTE href="http://localhost:4567/compute/408"><ID>408</ID><NAME>khaled</NAME><INSTANCE_TYPE>small</INSTANCE_TYPE><STATE>PENDING</STATE><DISK><STORAGE href="http://localhost:4567/storage/23" name="OpenFlowSwitch"/><TYPE>DISK</TYPE><TARGET>hda</TARGET></DISK><NIC><NETWORK href="http://localhost:4567/network/63" name="khaled"/><IP>10.142.100.1</IP><MAC>02:00:0a:8e:64:01</MAC></NIC></COMPUTE>khaled'
deb=ch.find('<ID>')+4
end=ch.find('</ID>')
id=ch[deb:end]
print id
deb=ch.find('<IP>')+4
end=ch.find('</IP>')
ip=ch[deb:end]
print ip



######## pour traiter le cas du hdfs
nch = """Configured Capacity: 25281294336 (23.55 GB)
Present Capacity: 22181785600 (20.66 GB)
DFS Remaining: 22181761024 (20.66 GB)
DFS Used: 24576 (24 KB)
DFS Used%: 0%
Under replicated blocks: 0
Blocks with corrupt replicas: 0
Missing blocks: 0

-------------------------------------------------
Datanodes available: 1 (1 total, 0 dead)

Name: 127.0.0.1:50010
Decommission Status : Normal
Configured Capacity: 25281294336 (23.55 GB)
DFS Used: 24576 (24 KB)
Non DFS Used: 3099508736 (2.89 GB)
DFS Remaining: 22181761024(20.66 GB)
DFS Used%: 0%
DFS Remaining%: 87.74%
Last contact: Tue Jun 21 05:51:36 PDT 2011


"""
debut=nch.find('%:')
fin=nch.find('%',debut+2)
resultat=float(nch[debut+3:fin])

print resultat






##### execution hdfs command
'''
from run_command import RunCommand
exe=RunCommand()
exe.do_add_host('157.159.103.101,vadmin,sector7g')
print('host added')
exe.do_connect()
res=exe.do_run('/usr/local/hadoop-0.20.2/bin/hadoop dfsadmin -report')

ch=res[4]
debut=ch.find(':')
fin=ch.find('%',debut)
val=float(ch[debut+1:fin])
print val


exe.do_close()
'''




##### echange de cle

'''
ip_mstr='157.159.103.116'
ip_slv='157.159.103.104\n157.159.103.240'

mstr=RunCommand()
mstr.do_add_host('157.159.103.116,vadmin,sector7g')
mstr.do_connect()
key=mstr.do_run("cd .ssh \nssh-keygen -q -t rsa -f id_rsa  -C '' -N ''")
print 'cle'
key_mstr=mstr.do_run('cat .ssh/id_rsa.pub')
print key_mstr
#cp=mstr.do_run('cp /home/vadmin/id_rsa* /home/vadmin/.ssh/')
slvList=['157.159.103.104,vadmin,sector7g','157.159.103.240,vadmin,sector7g']
key_slv=''

for i in slvList:
    slv=RunCommand()
    slv.do_add_host(i)
    slv.do_connect()
    print 'connected to slaves'
    exec_key_slv=slv.do_run("cd .ssh \nssh-keygen -q -t rsa -f id_rsa  -C '' -N ''")
    key_slv+=slv.do_run('cat .ssh/id_rsa.pub')[0]+'\n'
    #print key_slv
    inject_slv=slv.do_run('echo '+key_mstr[0]+'>.ssh/authorized_keys')
    scan_slv=slv.do_run('ssh-keyscan '+ip_mstr+'>.ssh/known_hosts')

print 'injection dans master'
print key_slv
inject_mstr=mstr.do_run("echo '"+key_slv+"'>.ssh/authorized_keys")
prep_scan_mstr=mstr.do_run("echo '"+ip_slv+"'>hosts")
scan_mstr=mstr.do_run("ssh-keyscan -f hosts>.ssh/known_hosts")

'''
'''
from extractVM import  VM
from exchange_keys import exchangeKeys
listVM=[]
h1='157.159.103.116'
h2='157.159.103.104'
h3='157.159.103.240'

v=VM()
v1=VM()
v2=VM()
v.host=h1
v.id=1
v.user='vadmin'
v.password='sector7g'
listVM.append(v)
v1.host=h2
v1.id=1
v1.user='vadmin'
v1.password='sector7g'

listVM.append(v1)
v2.host=h3
v2.id=1
v2.user='vadmin'
v2.password='sector7g'
listVM.append(v2)
for i in listVM:
    print i.host

o=exchangeKeys()
o.exchange(listVM)
'''

##########################config hdfs
'''
from extractVM import  VM
from exchange_keys import exchangeKeys
from run_command import RunCommand
listVM=[]
h1='157.159.103.101'
h2='157.159.103.104'
h3='157.159.103.240'

v=VM()
v1=VM()
v2=VM()
v.host=h1
v.id=1
v.user='vadmin'
v.password='sector7g'
listVM.append(v)
v1.host=h2
v1.id=1
v1.user='vadmin'
v1.password='sector7g'

listVM.append(v1)
v2.host=h3
v2.id=1
v2.user='vadmin'
v2.password='sector7g'
listVM.append(v2)

cs=open('core.log', 'r')
csList=cs.readlines()
csList[6]=csList[6].replace('IP_ADRESS',listVM[0].host)
csCh=''.join(csList)
print csCh
m=1
ip_slv=''
hdp_home='/usr/local/hadoop-0.20.2'

for vm in listVM:
    hst=vm.host+','+vm.user+','+vm.password
    slv=RunCommand()
    slv.do_add_host(hst)
    slv.do_connect()
    rt=slv.do_run("echo '"+csCh+"'>"+hdp_home+"/conf/core-site.xml")
    rt=slv.do_run("echo '"+listVM[0].host+"'>"+hdp_home+"/conf/masters")

'''
from config_mstr import configMstr

cf=configMstr()
listSlv=[]
listSlv.append('157.159.103.104')
listSlv.append('157.159.103.240')
ms='157.159.103.101'
cf.config(listSlv,ms,'vadmin','sector7g')