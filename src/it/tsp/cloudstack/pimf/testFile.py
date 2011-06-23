
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
from run_command import RunCommand
exe=RunCommand()
exe.do_add_host('157.159.103.116,vadmin,sector7g')
print('host added')
exe.do_connect()
res=exe.do_run('/usr/local/hadoop-0.20.2/bin/hadoop dfsadmin -report')

ch=res[4]
debut=ch.find(':')
fin=ch.find('%',debut)
val=float(ch[debut+1:fin])
print val


exe.do_close()

##### echange de cle

mstr=RunCommand()
mstr.do_add_host('157.159.103.116,vadmin,sector7g')
mstr.do_connect()
key=mstr.do_run("cd .ssh \nssh-keygen -q -t rsa -f id_rsa  -C '' -N ''")
print 'cle'
key=mstr.do_run('cat /home/vadmin/.ssh/id_rsa.pub')
print key
#cp=mstr.do_run('cp /home/vadmin/id_rsa* /home/vadmin/.ssh/')
