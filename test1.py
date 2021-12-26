from os import getenv
print("Hello world")
name = getenv("NAME")
if name == "Roni" :
    print("you are ok")
else:
    print("I don't know if you are ok")