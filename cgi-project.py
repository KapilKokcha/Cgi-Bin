#!/usr/bin/python36
import subprocess as sp
import cgi
print("Content-type: text/html")
print()

#print("hello <br />")
form=cgi.FieldStorage()
mainopt=form.getvalue("x")

if "run" and "basic" in mainopt:
		if "date" in mainopt:	#
	#	out=sp.getoutput("ansible all -m command -a date")
			out=sp.getoutput("sudo ansible localhost -m command -a date")	
			print(out)
		if "makefile" in mainopt:
			print(""" <form action='http://192.168.225.173/cgi-bin/touch_ansible.py'> 
			Where do you want to make file:<input name='m' /><br />
			Give content of file:<input name='i' /><br /> 
			<br /><input type='submit' />
			</form>  """)
		if "add user" in mainopt:
			print(""" <form action='http://192.168.225.173/cgi-bin/useradd_ansible.py'> 
			Give user name:<input name='m' /><br />
			Give user password:<input name='i' /><br /> 
			<br /><input type='submit' />
			</form>  """)
		if "delete user" in mainopt:
			print(""" <form action='http://192.168.225.173/cgi-bin/deluser_ansible.py'> 
			Give user name to delete:<input name='m' /><br /> 
			<br /><input type='submit' />
			</form>  """)
		if "change permission" in mainopt:
			print(""" <form action='http://192.168.225.173/cgi-bin/perchange_ansible.py'> 
			Give path:<input name='m' /><br /> 
			Give permission:<input name='i' /><br /> 
			<br /><input type='submit' />
			</form>  """)
		if "transfer file to ip" in opt:
			print(""" <form action='http://192.168.225.173/cgi-bin/perchange_ansible.py'> 
			Give IP:<input name='m' /><br /> 
			Give path of file to be transferred:<input name='i' /><br />
			Give path of position where to be copied:<input name='n' /><br /> 
			<br /><input type='submit' />
			</form>  """)
if "create partition" in mainopt:
	print(""" <form action='http://192.168.225.173/cgi-bin/create_partition.py'> 
		Give address of device (HDD):<input name='m' /><br /> 
		Give the no. of partitions to be made:<input name='i' /><br />
		Give the size of each partition(ex. 1GiB):<input name='n' /><br /> 
		<br /><input type='submit' />
		</form>  """)
if "create lvm" in mainopt:
	print(""" <form action='http://192.168.225.173/cgi-bin/create_lvm.py'> 
		Enter disk 1 (HDD):<input name='a' /><br /> 
		Enter disk 2 (HDD):<input name='b' /><br />
		Enter PE size(The size of the physical extent in megabytes.<br /> Must be a power
        	of 2.):<input name='c' /><br />
		Enter the vg name to be given:<input name='d' /><br />
		Enter the lv name to be given:<input name='e' /><br />
		Give the size of each partition:<input name='f' /><br /> 
		<br /><input type='submit' />
		</form>  """)
if "remove partition" in mainopt:
	print(""" <form action='http://192.168.225.173/cgi-bin/remove_partition.py'> 
		Enter disk who's partition to be removed (HDD):<input name='m' /><br /> 
		Enter partion number to be removed:<input name='i' /><br /> 
		<br /><input type='submit' />
		</form>  """)
if "mount the partition" in mainopt:
	print(""" <form action='http://192.168.225.173/cgi-bin/mount_partition.py'> 
		Enter the disk format(ex. ext4):<input name='m' /><br /> 
		Enter the disk to be mounted(ex. /dev/sdd):<input name='i' /><br />
		Enter the path where to mount(ex. /mnt/share):<input name='n' /><br /> 
		<br /><input type='submit' />
		</form>  """)
if "resize the lvm" in mainopt:
	print(""" <form action='http://192.168.225.173/cgi-bin/resize_lvm.py'> 
		Enter the name of VG:<input name='m' /><br /> 
		Enter the name of LV:<input name='i' /><br />
		Enter the size(ex. 512):<input name='n' /><br /> 
		<br /><input type='submit' />
		</form>  """)
if "mail" in mainopt:
	print(""" <form action='http://192.168.225.173/cgi-bin/mail.py'> 
		Enter hosts :<input name='a' /><br /> 
		Enter port (587):<input name='b' /><br />
		Enter mailid :<input name='c' /><br />
		Enter password:<input name='d' /><br />
		Mail to:<input name='e' /><br />
		Subject:<input name='f' /><br />
		Body:<input name='g' /><br /> 
		<br /><input type='submit' />
		</form>  """)
if "allow the service" in mainopt:
	print(""" <form action='http://192.168.225.173/cgi-bin/allow_service.py'> 
		Enter the port no to allow:<input name='m' /><br /> 
		<br /><input type='submit' />
		</form>  """)
if "launch docker" in mainopt:
	print(""" <form action='http://192.168.225.173/cgi-bin/dock/17juned.py'> 
		Press submit to continue<br />  
		<br /><input type='submit' />
		</form>  """)
'''	print(""" <form action='http://192.168.225.173/cgi-bin/launch_docker.py'> 
		Enter docker name:<input name='m' /><br /> 
		Enter image name:<input name='i' /><br /> 
		<br /><input type='submit' />
		</form>  """)
'''
if "launch ec2" in mainopt:
	print(""" <form action='http://192.168.225.173/cgi-bin/mail.py'> 
		Enter key name :<input name='a' /><br /> 
		Enter Region :<input name='b' /><br />
		Instance_type :<input name='c' /><br />
		Image :<input name='d' /><br />
		vpc_subnet_id :<input name='e' /><br />
		aws_access_key :<input name='f' /><br />
		aws_secret_key :<input name='g' /><br />
		assign_public_ip :<input name='x' /><br /> 
		<br /><input type='submit' />
		</form>  """)
if "launch webserver" in mainopt:
	print(""" <form action='http://192.168.225.173/cgi-bin/launch_webserver.py'> 
		Enter server name:<input name='m' /><br />  
		<br /><input type='submit' />
		</form>  """)
if "create vdo" in mainopt:
	print(""" <form action='http://192.168.225.173/cgi-bin/create_vdo.py'> 
		enter the vdo name to be given:<input name='m' /><br /> 
		enter the drive path you want it to make on vdo:<input name='i' /><br />
		enter the size of vdo to be made:<input name='n' /><br /> 
		<br /><input type='submit' />
		</form>  """)
if "remove vdo" in mainopt:
	print(""" <form action='http://192.168.225.173/cgi-bin/remove_vdo.py'> 
		enter the name of vdo to be removed:<input name='m' /><br />  
		<br /><input type='submit' />
		</form>  """)
if "manage docker" in mainopt:
	print(""" <form action='http://192.168.225.173/cgi-bin/dock-html/run.py'> 
		Press submit to continue<br />  
		<br /><input type='submit' />
		</form>  """)
