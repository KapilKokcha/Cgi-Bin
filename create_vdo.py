#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type: text/html")
print()

form=cgi.FieldStorage()
u=form.getvalue("m")
v=form.getvalue("i")
w=form.getvalue("n")
print(u)
print(v)
print(w)
z=open("/var/www/cgi-bin/yml_files/i_touch_ansible.yml","w")
z.write("x: {}\n".format(u))
z.write("y: {}\n".format(v))
z.write("s: {}".format(w))
z.close()

x=sp.getoutput("sudo ansible-playbook /var/www/cgi-bin/yml_files/vdo_ansible.yml")
print("success")
