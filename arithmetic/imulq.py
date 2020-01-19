def imulq(string):
    if ("imulq" in string):
        str0 = string.split(",")[0].strip().split("imulq")[1].strip()
        str1 = string.split(",")[1].strip()
        print("{0} = {0} unsigned multiplicate (*) {1}".format(str1, str0), end = "")