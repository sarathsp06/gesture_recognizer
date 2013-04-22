#!/usr/bin/python
import virtkey
import time
import sys
def simulate():
    v = virtkey.virtkey()
    while True:
    	time.sleep(1)
    	v.press_unicode(ord("a"))
   	v.release_unicode(ord("a"))
    	v.press_keysym(65363)
    	v.release_keysym(65363)
    pass
def stroke(key):

	keys={"LEFT":155,"RIGHT":0x27,"HOME":0x24,"END":0x23}
	v = virtkey.virtkey();
	v.press_unicode(keys[key])
	v.release_unicode(keys[key])


if __name__=='__main__':
    stroke(sys.argv[1])
    
