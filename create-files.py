for i in range (10):
    f = open("output/fileeeee-%d.txt" % (i+1),"w+") 
    print("fileeeee-%d.txt Created!" % (i+1))
    for i in range(5):
     f.write("This is line %d\r\n" % (i+1))
    f.close()
