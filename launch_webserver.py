#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type: text/html")
print()

form=cgi.FieldStorage()
u=form.getvalue("m")
print(u)


sp.getoutput("docker run -dit --name {} webserver".format(u))
print("success")
