"""import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('157.159.103.101', username='vadmin',password='sector7g')
stdin, stdout, stderr = ssh.exec_command("ls /home/")
stdin.close()
data = stdout.read().splitlines()
for line in data:
    print line
"""
from run_command import RunCommand
from extract_cmd import TransformXmlToCmd, Cmd
from extractVM import TransformXmlToVM, VM
from extract_value import obj_extract



#extracting list of vms that will be used to extract values
vmObj = TransformXmlToVM()
vmObj.readXml('/home/khaled/listeVMsTest.xml')
vms = vmObj.getVM()
v = "%s,%s,%s" % (vms[0].host, vms[0].user, vms[0].password)
print 'VM:'
print v



#extracting of command from xml file:
cmdCl = TransformXmlToCmd()
cmdCl.readXml('/home/khaled/cmdCrTest.xml')

#preapring list of indicator used
listCr = []
listCr.append('disk')
cmd = cmdCl.getcmd(listCr)
#cmd is a list containing objects that contain the indicator and her command
print 'commande extraite'
print cmd[0].cmd
print cmd[0].tempsExt
#preparing connexion to run commands
cnx = RunCommand()
cnx.do_add_host('157.159.103.101,vadmin,sector7g')
cnx.do_connect()
host='157.159.103.101,vadmin,sector7g'
cmde="df -h | grep '^/'"
#Excuting command on remote host
print 'execution'
r = cnx.do_run("df -h | grep '^/'")
print"'affichage"
print r[0]

print'fin exec'

rt= r[0].split("G")
print float(rt[1])
print '.:fin test simple cmd:. \n .:debut test extract:.'

ex=obj_extract()
ex.extract(host,cmd[0],'disk')





