# def add(a,b):
#  return (a+b);
#
#  def minus (x,y):
#        return  x-y;
#        print(minus(9,4))

# Lambda functions or anonymous functions
def add(a, b):
    return a+b
print(add(3,5))

minus = lambda x, y: x-y

def minus(x, y):
    return x-y

print(minus(9, 4))


a = [[1, 14], [5, 6], [8, 23]]
a.sort(key=lambda x: x[1])
print(a)

