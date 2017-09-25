si = 0
ci = 0

while True:

    inp = raw_input("Enter a number: ")
    if inp == 'done' : break
    try:
        num = float(inp)
        si = si + num
        ci = ci + 1
    except: #this appears to also work for an unintended blank line of data as well.
        print "Bad Data"
    if ci != 0 :
      print "Sum:", si, "Count:", ci, "Mean:",si/ci
    else :
      print "All inputs you entered were invalid ! Good Bye !"    
 
print "Sum:", si, "Count:", ci, "Mean:",si/ci