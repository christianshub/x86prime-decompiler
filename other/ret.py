def ret(string):
    if ("ret" in string):
        ret = string.split(" ")[1].strip()
        print("return {0}".format(ret), end = "")

# string = "ret %r11"
# ret(string)