#------------for int------------------
def gen(n):
    for i in range(n):
        yield  i
g=gen(4)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())

#-----------for string----------------
h="harry"
ier=iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())

