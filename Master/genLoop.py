import test

text = input("True(t) or False(f)?")
while (text == "t"):
    print("Calling test.py")
    try:
        execfile("test.py")
    except NameError:
        exec(open("test.py").read())
    text = input("True(t) or False(f)?")
