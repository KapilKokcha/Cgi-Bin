#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type: text/html")
print()

form=cgi.FieldStorage()
u=form.getvalue("m")
v=form.getvalue("i")
print(u)
print(v)
z=open("/var/www/cgi-bin/yml_files/i_touch_ansible.yml","w")
z.write("x: {}\n".format(u))
z.write("y: {}".format(v))
z.close()

sp.getoutput("sudo ansible-playbook /var/www/cgi-bin/yml_files/useradd_ansible.yml --become-user=root")
print("success")
