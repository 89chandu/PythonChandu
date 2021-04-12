f=open("chandu.txt")
content = f.read()
print(content)
f.close()

f=open("chandu.txt","rt")
print(f.readline())
f.close()

f=open("chandu.txt","w")
f.write("chandu bhai kee baat hee alag hai")
f.close()

f=open("chandu.txt", "r+")
print(f)