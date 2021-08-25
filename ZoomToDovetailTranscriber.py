import re
import sys

infile = open(sys.argv[1], 'r')

def replacer(matchobj):
    name = matchobj.group(0).replace(':','')
    return '<v %s>' % name

outcontent = ''
for line in infile:
  stripline = line.strip()
  newline = re.sub(r'([a-zA-Z].*?:)', replacer, stripline)
  outcontent += newline + '\n'
infile.close()

outfileName = sys.argv[1].replace(".vtt", "_fordovetail.vtt")
outfile = open(outfileName, 'w')
outfile.write(outcontent)
outfile.close()
