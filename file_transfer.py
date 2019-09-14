#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type: text/html")
print()

form=cgi.FieldStorage()
ip=form.getvalue("m")
path=form.getvalue("i")
path2=form.getvalue("n")
print(ip)
print(path)
print(path2)
#z=open("/var/www/cgi-bin/yml_files/i_touch_ansible.yml","w")
#z.write("x: {}\n".format(u))
#z.write("y: {}".format(v))
#z.close()

#sp.getoutput("sudo ansible-playbook /var/www/cgi-bin/yml_files/useradd_ansible.yml --become-user=root")
sp.getoutput("scp {0} {1}:{2}".format(ip,path,path2))
print("success")
