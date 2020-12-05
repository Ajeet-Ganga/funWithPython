import os
import pathlib
import datetime

root_dir = '.'

# This prints all the file in root_dir in the format of  "YYYY/MM/DD | DIRECTORY | FILENAME"
for directory, subdirectories, files in os.walk(root_dir):
    for file in files:
    	fname = os.path.join(directory, file)
        if (pathlib.Path(fname)):
        	ts_epoch = os.path.getmtime(fname)
        	ts = datetime.datetime.fromtimestamp(ts_epoch).strftime('%Y/%m/%d')
        	# print ts + " | " + fname 
        	print ",".join([ts,directory, file])
        else:
        	print 'ERROR: File doesnt exist. file name =' + fname
