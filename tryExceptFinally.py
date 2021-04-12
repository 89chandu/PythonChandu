f1=open("harry.txt")
try:
    f1=open("does.txt")

except: Exception as e:
print(e)

    else:
    print("this will run only if except not run ")

                     finally:
                    print("run anyway")
                    f1.close()
