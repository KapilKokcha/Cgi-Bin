import subprocess as sp

sp.getoutput("docker run -dit --name os_firefox firefox_saas")


"""fs=open("/etc/ssh/sshd_config","r")
fs1=open("/rootDesktop/abc","a")

fs.seek(0,0)
s=fs.readline()
#a=fs1.readline()
if s=="# X11UseLocalHost yes":
	s="X11UseLocalHost no"
	fs1.append(s)
else:
	fs1.append(s)
fs.close()
fs1.close()"""



