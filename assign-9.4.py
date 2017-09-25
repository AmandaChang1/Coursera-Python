
counts=dict()
name=raw_input('enter a file:') 
if len(name)==0:
    name="mbox-short.txt"
fh=open(name)
for line in fh:
    if not line.startswith('From:'):continue
    line=line.split()
    words=line[1]
    words=words.split() 
    for word in words:
        counts[word]=counts.get(word,0)+1

    maxv=None
    maxk=None
    for k,v in counts.items():
        if maxv==None or maxv<v:
          maxv=v
          maxk=k
print maxk,maxv