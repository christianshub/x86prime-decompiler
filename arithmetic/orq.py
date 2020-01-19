def orq(string):
    if ("orq" in string) and not ("xorq" in string):
        str0 = string.split(",")[0].strip().split("xorq")[1].strip()
        str1 = string.split(",")[1].strip()
        print("{0} = {0} bitwise or (|) {1}".format(str1, str0), end = "")