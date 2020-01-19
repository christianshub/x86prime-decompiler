def addq(string):
    if "addq" in string:
        str0 = string.split(",")[0].strip().split("addq")[1].strip()
        str1 = string.split(",")[1].strip()
        print("{0} = {0} add (+) {1}".format(str1, str0), end = "")