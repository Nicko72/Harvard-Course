# Nick May  - Harvard Course - May 2021

# Decorator - function that can run another function

def announce(f):
    def wrapper():
        print("About to run the function . . . . . .")
        f()
        print("Done with the function")
    return wrapper

@announce # this is the key line where the function is wrapper in another function.
def hello():
    print("Hello World!")

# now the hello function goes into the announce function first. It is wrapper inside the announce / wrapper and run within it.

hello()