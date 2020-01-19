def xorq(string):
    if "xorq" in string:
        str0 = string.split(",")[0].strip().split("xorq")[1].strip()
        str1 = string.split(",")[1].strip()
        print("{0} = {0} bitwise xor (^) {1}".format(str1, str0), end = "")