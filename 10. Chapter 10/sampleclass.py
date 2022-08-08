class Sample :
    a = "Harry" # Class Attribute


obj = Sample()
obj.a = "Vicky" #instance attribute
#Sample.a = "Vicky" # changes class attribute
print(Sample.a)
print(obj.a)