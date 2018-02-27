# 
# run this code:
# mpirun --hostfile file ThingToRun
#

#import subprocess

# the file
f = raw_input("File: ")

# what you will run
thingToRun = raw_input("What you are running: ")

subprocess.call(["mpirun", "--hostfile", f, thingToRun], shell = True)


