import time
import os
print("round 1")
for i in range (10):
    f= open("output/bla-file-%d.txt" % (i+1),"w+") 
    print("file-%d.txt Created!" % (i+1))
    for i in range(5):
     f.write("This is line %d\r\n" % (i+1))
    f.close()
    time.sleep(10)
    
# time.sleep(300)
# print("round 2")
# for i in range (10):
#     f= open("output/bla-fileeee-%d.txt" % (i+1),"w+") 
#     print("file-%d.txt Created!" % (i+1))
#     for i in range(5):
#      f.write("This is line %d\r\n" % (i+1))
#     f.close()
#     time.sleep(10)
