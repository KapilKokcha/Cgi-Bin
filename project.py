#!/usr/bin/python36
import subprocess as sp
import cgi
print("Content-type: text/html")
print()

print("hello <br />")
form=cgi.FieldStorage()
mainopt=form.getvalue("x")
opt=form.getvalue("y")
if "run basic command" in mainopt:
	print("Select command you want to run<br />")
	print("""<form>
	<select name='opt'>
	<option>date</option>
	<option>user</option>
	</form>
	<input type='submit'>""")
	if "date" in opt:	#
	#	out=sp.getoutput("ansible all -m command -a date")
		out=sp.getoutput("date")	
		print(out)
	if "makefile" in opt:
		sp.getoutput("ansible-playbook touch_ansible.yml")
	if "add user" in opt:
		sp.getoutput("ansible-playbook useradd_ansible.yml")
	if "delete user" in opt:
		sp.getoutput("ansible-playbook deluser_ansible.yml")
	if "transfer file to ip" in opt:
		ip=input()
		path=input("give path of file to be transferred")
		path2=input("give path of position where to be copied")
		sp.getoutput("scp {0} {1}:{2}".format(ip,path,path2))
	if "change permission" in opt:
		sp.getoutput("ansible-playbook perchange_ansible.yml")
	if "copy the content" in opt:
		print(opt)
		print("1")
		fp=open('/root/Desktop/ansible_project/input.yml',mode='a')
		data = csession.recv(50)
		a = data.decode()
		data1 = csession.recv(50)
		b = data1.decode()
		print(a)
		print(b)
		fp.write("x: {}\n".format(a))
		fp.write("y: {}".format(b))
		fp.close()
		sp.getoutput("ansible-playbook /root/Desktop/ansible_project/copycontent_ansible.yml")

"""	
	if "create partition" in mainopt:
		sp.getoutput("ansible-playbook partition_ansible.yml")
	
	if "create lvm" in mainopt:
		sp.getoutput("ansible-playbook lvm_ansible.yml")
	
	if "remove partition" in mainopt:
		sp.getoutput("ansible-playbook removepart_ansible.yml")
	
	if "mount the partition" in mainopt:
		sp.getoutput("ansible-playbook mount_ansible.yml")
	
	if "resize the lvm" in mainopt:
		sp.getoutput("ansible-playbook resizelvm_ansible.yml")
	

	if "mail" in mainopt:
		sp.getoutput("ansible-playbook mail_ansible.yml")
	
	if "allow the service" in mainopt:
		sp.getoutput("ansible-playbook firewall_ansible.yml")
	
	if "launch docker" in mainopt:
		sp.getoutput("ansible-playbook docker_proj.yml")
	
	if "launch ec2" in mainopt:
		sp.getoutput("ansible-playbook ec2_ansible.yml")
	
	if "launch webserver" in mainopt:
		sp.getoutput("python36 webserver.py")
	
	if "create vdo" in mainopt:
		sp.getoutput("ansible-playbook vdo_ansible.yml")
	
	if "remove vdo" in mainopt:
		sp.getoutput("ansible-playbook vdoremove_ansible.yml")
		
	if out=="":
		output="Successfully Done"
	else:
		output=out
	csession.send(output.encode())



"""
