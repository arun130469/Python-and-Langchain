def parameterized_decorator(param):
    print(f"1: parameterized_decorator CALLED with param={param}")
    def actual_decorator(func):
        print("2: actual_decorator CALLED with", func.__name__)
        def wrapper(*args, **kwargs):
            print("3: wrapper CALLED")
            return func(*args, **kwargs)
        print("4: actual_decorator RETURNS wrapper (replaces original)")
        return wrapper
    print("5: parameterized_decorator RETURNS actual_decorator")
    return actual_decorator

@parameterized_decorator("X")
def hello():
    print("6: hello CALLED")

hello()


# What happens?
# When Python loads the file:
##  parameterized_decorator("X") is called.
##  Prints: 1: parameterized_decorator CALLED with param=X

##  It returns actual_decorator, not wrapper yet.
##  Prints: 5: parameterized_decorator RETURNS actual_decorator

##  actual_decorator(hello) is called next.
##  Prints: 2: actual_decorator CALLED with hello

##  It returns wrapper, so hello = wrapper
##  Prints: 4: actual_decorator RETURNS wrapper (replaces original)

# When you call hello():
## Actually runs wrapper().
## Prints: 3: wrapper CALLED

## Inside, func(*args, **kwargs) calls the real hello.
## Prints: 6: hello CALLED
