#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type: text/html")
print()

form=cgi.FieldStorage()
u=form.getvalue("m")
print(u)
z=open("/var/www/cgi-bin/yml_files/i_touch_ansible.yml","w")
z.write("x: {}".format(u))
z.close()

x=sp.getoutput("sudo ansible-playbook /var/www/cgi-bin/yml_files/firewall_ansible.yml")
print("success")
