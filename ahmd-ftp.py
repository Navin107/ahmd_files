import os
from subprocess import call,Popen,PIPE


cmd = "git status"

process = Popen(cmd, shell=True)
process.communicate ()

cmd = "git add . "

process = Popen(cmd, shell=True)
process.communicate ()
cmd = "git commit -m 'newfiles added' "

process = Popen(cmd, shell=True)
process.communicate ()
