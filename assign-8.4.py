
words=list()
fname=raw_input('Enter file name:')
if len(fname) == 0:
    fname="romeo.txt"
fh=open(fname)
for line in fh:
    for word in words:
    if word:continue
    else:
      word=words.append()
words.sort()      
print words