import json
import datetime
import os

#FIXME
file_prefix='/home/bano/my_media/nemesis/vertical/07-09-2017/cwmp/'

folder_proc='proc/meta/'
cmd='mkdir -p %s' %(file_prefix+folder_proc)
os.system(cmd)

file_output=file_prefix+folder_proc+"cwmp.meta"
fOut = open(file_output, 'w')

blocks=["block1","block2","block3","block4","block5","block6","block7"]

fOut.write("ZGRAB\n")

# ======== ZMAP (TCP) =========
for block in blocks:
	file_tcp=file_prefix+block+'/out_tcp/meta.log'
	file_cwmp=file_prefix+block+'/out_cwmp/meta.log'
	with open(file_tcp) as data_file:
	    tcp = json.load(data_file)
	
	# ======== ZGRAB (CWMP) =========
	fOut.write(block+"\n")
	with open(file_cwmp) as data_file:
	    cwmp = json.load(data_file)
	
	if tcp["success_unique"]-cwmp["total"]==0:
		fOut.write("Unsent\tnil\n")
	else:
		fOut.write("Unsent\t%d\n" %(tcp["success_unique"]-cwmp["total"]))
	fOut.write("200OK\t%0.2f%%\n" %(float(cwmp["success_count"])/float(cwmp["total"])*100))
	fOut.write("Other\t%0.2f%%\n" %(float(cwmp["failure_count"])/float(cwmp["total"])*100))
	fOut.write("Duration\t%d seconds\n" %(cwmp["duration"]))
	fOut.write("\n=====\n\n")

fOut.close()
