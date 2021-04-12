
class A:
    classvar1 = "I am a class variable in class A"  # yah Ek Class varriable hai
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"   # ---  yah ek instance varriable hai
        self.special = "Special"

class B(A):
    classvar1 = "I am in class B"

    def __init__(self):
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"   # yah ek instance varriable ahi jo sabse phle run hota hai...
        super().__init__() #  iska mtlb super class ke init ko run kro....
        print(super().classvar1)


a = A()
b = B()

print(b.special, b.var1, b.classvar1)


#     ----- pahle instance varriable run hota hai uske baad me class varriable run hota hai but
#     hume yadi phir bhi class varriable ko run karna hai tab num super keyword ka use karte hai

