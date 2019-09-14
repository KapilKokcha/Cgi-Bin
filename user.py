#!/usr/bin/python36
import subprocess as sp
import cgi
print("Content-type: text/html")
print()

form=cgi.FieldStorage()
u=form.getvalue("x")
print(u)
#l=sp.getoutput("sudo useradd {}".format(u))
#print("user added")
#print(x)
#print("hiii")
print(u)
