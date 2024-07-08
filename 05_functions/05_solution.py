# if parameter not passes we use default value.
def greet(name = "User"):
    return "Hello, " + name + " !"


print(greet("chai"))
print(greet())