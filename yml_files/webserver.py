import subprocess as sp

user=input("give user name")
sp.getoutput("docker run -dit --name {} webserver".format(user))
