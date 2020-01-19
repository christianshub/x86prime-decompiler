def andq(string):
    if "andq" in string:
        str0 = string.split(",")[0].strip().split("andq")[1].strip()
        str1 = string.split(",")[1].strip()
        print("{0} = {0} bitwise and (&) {1}".format(str1, str0), end = "")