# '''
# LEGB -- Local, EnClosing, Global, Built-ins'''
import builtins

# x = 'global-x'

# def test():
#     # y ='local-y'
#     # print(y)
#     global x # Declare x as a Global Variable 
#     x = 'local-x'
#     print(x)

# test()

# print(y) # Y not Found in outside the Function . Because its a Local Variable

# print(x) # This will Print the Global x


# def test(z):
#     x = 'local-x'
#     print(z)

# test('local-z')

# def min():
#     pass

# m = min([4,5,1,2,3])
# print(m)

# print(dir(builtins))

# !!! Enclosing Functions !!!!

def outer():
    x = 'outer-x'
    def inner():
        # x ='inner-x' # if we comment out the Line . print(x) line not find x in local scope 
        #but found x in enclosing scope.

        nonlocal x
        x = 'inner-x'
        print(x)

    inner()
    print(x)

outer()


