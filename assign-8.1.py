
words=list()
fname=raw_input('Enter file name:')
if len(fname) == 0:
    fname="romeo.txt"
fh=open(fname)
for line in fh:
    line=line.strip().split()
    words=words+line
words.sort()
print words