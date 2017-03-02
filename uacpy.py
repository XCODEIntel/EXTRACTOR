# dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de 
#dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de 
#dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de 
#dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de 
#dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de 
# dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de 
#dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de 
#dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de 
#dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de 
#dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de 
# dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de 
#dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de 
#dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de 
#dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de 
#dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de 
# dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de 
#dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de 

import os
import subprocess
import time
import sys


def  mainc():
	try:
		feku=open('listoffiles.txt','r')
		sd=feku.readlines()
		#print 'ds'
		for zxs in sd:
			zxs=zxs.strip()
			#print 'ds2'
			jk=zxs.split('\\')
			#print 'ds3'
			lk=len(jk)
			jk=jk[lk-1]
			processtorun=' -extract '+zxs+' '+os.getcwd()+os.sep+jk
			#print 'ds1'
			fgetpathh=os.environ['TEMP']+os.sep+'zextr.exe'

			print fgetpathh
			print processtorun

		
			try:
				os.system(fgetpathh+processtorun)
			except Exception as ex:
				print ex
				print 'Unable to fetch file'+jk
			
	except Exception as ex:
		print ex
		

mainc()



