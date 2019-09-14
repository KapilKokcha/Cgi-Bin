#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type: text/html")
print()

form=cgi.FieldStorage()
h=form.getvalue("a")
i=form.getvalue("b")
j=form.getvalue("c")
k=form.getvalue("d")
l=form.getvalue("e")
m=form.getvalue("f")
n=form.getvalue("g")
print(u)
print(v)
z=open("/var/www/cgi-bin/yml_files/i_touch_ansible.yml","w")
z.write("o: {}\n".format(h))
z.write("p: {}\n".format(i))
z.write("q: {}\n".format(j))
z.write("r: {}\n".format(k))
z.write("s: {}\n".format(l))
z.write("t: {}\n".format(m))
z.write("u: {}".format(n))
z.close()

x=sp.getoutput("sudo ansible-playbook /var/www/cgi-bin/yml_files/mail_ansible.yml")
print("success")
