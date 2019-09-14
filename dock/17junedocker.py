#!/usr/bin/python36 
import subprocess
import cgi

print("content-type: text/html")
print() 

form = cgi.FieldStorage() 
docker_name = form.getvalue("n") 
docker_image = form.getvalue("img")
#docker_remove=form.getvalue("m")
docker_run = "sudo docker run -d -i -t --name {} {}".format(docker_name , docker_image)
subprocess.getoutput(docker_run)
print("your docker {} has been launched".format(docker_name))
print("<br />Manage dockers <a href=http://192.168.225.173/cgi-bin/dock-html/run.py>run</a>")
#docker_stop="sudo docker stop {}".format(docker_remove)
#docker_rm="sudo docker rm {}".format(docker_remove)
#y = subprocess.getoutput(docker_remove)
#print(y)
