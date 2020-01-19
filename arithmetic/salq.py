def salq(string):
    if ("salq" in string):
        str0 = string.split(",")[0].strip().split("salq")[1].strip()
        str1 = string.split(",")[1].strip()
        print("{0} = {0} shift left (<<) {1} (k)".format(str1, str0), end = "")