#!/usr/bin/python36
print("content-type: text/html")
print()

import subprocess as sp
x=sp.getoutput("sudo ansible localhost -m command -a date")
y=x[29:]
print(y)

#y=x.split('\n')
#print(y)
