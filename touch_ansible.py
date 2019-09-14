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

sp.getoutput("sudo ansible-playbook /var/www/cgi-bin/yml_files/touch_ansible.yml")
print("success")

"""
>>> x=open("/root/Desktop/abc.txt","w")
>>> x.write("hiiiii")
6
>>> x.close()
>>> x=open("/root/Desktop/abc.txt","w")
>>> y="hiii"
>>> x.write
<built-in method write of _io.TextIOWrapper object at 0x7f32ab5e0558>
>>> x.write(y)
4
>>> x.close()
"""
