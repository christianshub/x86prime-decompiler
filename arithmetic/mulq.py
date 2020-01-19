def mulq(string):
    if ("mulq" in string) and not ("imulq" in string):
        str0 = string.split(",")[0].strip().split("mulq")[1].strip()
        str1 = string.split(",")[1].strip()
        print("{0} = {0} signed multiplicate (*) {1}".format(str1, str0), end = "")