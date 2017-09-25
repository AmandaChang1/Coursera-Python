
count=0
fname=raw_input('Enter file name:')
if len(fname)==0:
    fname="mbox-short.txt"
fh=open(fname)
for line in fh:
    line=line.rstrip()
    if not line.startswith('From:'):continue
    list=line.split()
    count=count+1   
    print list[1]
  
print "There were", count, "lines in the file with From as the first word"
