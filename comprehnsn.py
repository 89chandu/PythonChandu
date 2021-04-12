ls=[]
for i in range(100):
       if i%3==0:
         ls.append(i)

 #----------------using list comprehenssion----------------

ls=[i for i in range(100)]
print(ls)

#----------------dictionary comprehenssion------------

dict1= { i ==f"item{i}" for i in range(100)}
print(dict1)

#-------------------set comprehession-----------------------

dresses = {dress for dress in
                      ["dress1","dress2","dress1","dress2"]}
print(dresses)

