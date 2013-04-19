import os
a=os.fork();
if a == 0:
	os.system('./pro.py run')
exit()
