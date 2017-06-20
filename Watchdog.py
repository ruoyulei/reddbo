import subprocess
import time
import os

if __name__ == '__main__':
	cmd = 'ps -ef'
	proc = 'python main.py'
	while 1:
		flag = False
		out = subprocess.check_output(cmd, shell=True)
		line = out.splitlines()
		for a in line:
			if proc in a:
				flag = True

		if flag:
			time.sleep(60)
		else:
			print 'starting service'
			os.system('python main.py &')
