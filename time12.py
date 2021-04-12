import  time
intial = time.time()

k=0
while(k<45):
    print("this is me")
    k+=1
print("while loop time",time.time()-intial,"seconds")

intial2=time.time()

for i in range (45):
    print("this is me")
   # time.sleep(2)
print("foor loop",time.time()-intial2,"seconds")