

# def outer_function():
#     message='Hi'

#     def inner_function():
#         print(message)

#     return inner_function


# my_func = outer_function() # my_func equal to the inner function but not Executed

# # Execute my_func
# my_func()
# my_func()
# my_func()
# my_func()


# def outer_function(msg):

#     def inner_function():
#         print(msg)

#     return inner_function


# my_func = outer_function("Hello Sohel")

# my_func()
# my_func()
# my_func()


# !!! Decorator Definition Below !!!

def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args,**kwargs)

    return wrapper_function


# def display():
#     print('Display Function ran')
# decorated_display = decorator_function(display) # Function is Ready to Execute

# decorated_display() # Function Execution

# !!! Now the Fun Main Thing of Decorators is !!!
# @decorator_function
# def display():
#     print('Display Function ran')

# display()

# @decorator_function
# def display_info(name,age):
#     print('Display info rans with arguments {} and {} '.format(name,age))

# display_info('Sohel',32)



# !!! Decorator Class !!!

# class DecoratorClass:

#     def __init__(self,original_function):
#         self.original_function = original_function

#     def __call__(self,*args,**kwargs):
#         print('call method executed this before {}'.format(self.original_function.__name__))
#         return self.original_function(*args,**kwargs)


# @DecoratorClass
# def display_info(name,age):
#     print('Display info rans with arguments {} and {} '.format(name,age))

# display_info('Sohel',32)





# !!! Logger Example !!!

# def my_logger(original_function):
#     import logging

#     logging.basicConfig(filename='{}.log'.format(original_function.__name__),level=logging.INFO)

#     def wrapper(*args,**kwargs):
#         logging.info('Ran with args: {} and kwargs: {}'.format(args,kwargs))
#         return original_function(*args,**kwargs)

#     return wrapper


# @my_logger
# def display_info(name,age):
#     print('Display info rans with arguments {} and {} '.format(name,age))

# display_info('Rashin',28)


# !!! Timing Function Example !!!

def my_timer(original_function):
    import time

    def wrapper(*args,**kwargs):
        t1= time.time()
        result = original_function(*args,**kwargs)
        t2 = time.time()-t1
        print('{} ran in {} sec'.format(original_function.__name__,t2))
        return result

    return wrapper


@my_timer
def display_info(name,age):
    print('Display info rans with arguments {} and {} '.format(name,age))

display_info('Rashin',28)

