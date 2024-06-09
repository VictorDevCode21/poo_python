# Decorators
# Python receives a function and adds some functionality before or after his execution



# def Decorator(function):
#     def modified_function():
#         print("Before calling the function")
#         function()
#         print("After calling the function")
#     return modified_function()


# def SayHi():
#     print("Hi five")

# Decorator(SayHi)


def Decorator(function):
    def modified_function():
        print("Before calling the function")
        function()
        print("After calling the function")
    return modified_function

@Decorator
def SayHi():
    print("Hi five")

SayHi()