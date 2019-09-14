#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type: text/html")
print()

form=cgi.FieldStorage()
k=form.getvalue("a")
l=form.getvalue("b")
m=form.getvalue("c")
n=form.getvalue("d")
o=form.getvalue("e")
p=form.getvalue("f")
print(u)
print(v)
z=open("/var/www/cgi-bin/yml_files/i_touch_ansible.yml","w")
z.write("r: {}\n".format(k))
z.write("s: {}\n".format(l))
z.write("t: {}\n".format(m))
z.write("u: {}\n".format(n))
z.write("v: {}\n".format(o))
z.write("w: {}".format(p))
z.close()


x=sp.getoutput("sudo ansible-playbook /var/www/cgi-bin/yml_files/lvm_ansible.yml")
print("success")
