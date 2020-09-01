def largenum(x):

    #"""
    #x is a large number

    #"""

    #return x * 200

    if __name__ == "__main__":

       print("Hello Python")
       y = int(input("Enter a number"))
       print(y, largenum(y))

def func_return(a, b):
    return a + b, a * b, a / b

Z = func_return(12, 6)

print(Z)
print(type(Z))


