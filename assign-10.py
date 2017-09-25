
name=raw_input("enter a file:")
if len(name)==0:
    name="mbox-short.txt"
fh=open(name)
counts=dict()
for line in fh:
    if not line.startswith("From"):continue 
    line=line.split()
    words=line[5:6]    
   
    for word in words:
        wrd=word[:2]
        counts[wrd]=counts.get(wrd,0)+1
        
flipped=list()
for k, v in counts.items():
    newtup=(k,v)
    flipped.append(newtup)
    
flipped.sort(reverse=True)    
for k, v in flipped[:]:
    print k,v 