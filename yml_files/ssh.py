import subprocess as sp
import os

user=input()
os.system("ssh {}".format(user))
