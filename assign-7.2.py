# Use the file name mbox-short.txt as the file name
si = 0
ci = 0
fname=raw_input('Enter file name:')
if len(fname) == 0:
    fname="mbox-short.txt"
fh=open(fname)
for line in fh:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line[20:]
    num = float(line[20:])
    si = si + num
    ci = ci + 1   
print "Average spam confidence:", si/ci 
