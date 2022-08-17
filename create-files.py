import time
for i in range (3):
    ts = time.time()
    f = open("output/file-{}-{}.txt".format(ts,i+1),"w+") 
    print("file-{}-{}.txt Created!".format(ts,i+1))
    for i in range(5):
     f.write("This is line %d\r\n" % (i+1))
    f.close()
    time.sleep(500)

    
    
   
