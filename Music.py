import os, time, glob, random

name = '/home/pandey/Music/'

list = glob.glob(name+'*/*')

def play():
	
	num = random.randint(1, len(list))

	name = "mpg321 %s"%(list[num])
	
	os.system(name)