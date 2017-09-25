largest = 0
smallest = None
         
while True:
   inp=raw_input("enter a number")
   if inp== "done" : break 
   if len(inp)<1 : break 
   try:
      num=int(inp)
   except:  
      print "Invalid input" 
      continue
   if num>largest:largest=num                   
   if smallest is None or num<smallest:smallest=num
                            
print 'Maximum is',largest
print 'Minimum is',smallest