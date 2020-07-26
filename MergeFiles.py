import shutil
import time
import glob


outfilename = 'MasterURL' + ".txt"

filename = glob.glob('*.txt')

with open(outfilename, 'wb') as outfile:
    for filename in glob.glob('*.txt'):
        if filename == outfilename:
            # don't want to copy the output into the output
            continue
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)
