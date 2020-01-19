def sarq(string):
    if ("sarq" in string):
        str0 = string.split(",")[0].strip().split("sarq")[1].strip()
        str1 = string.split(",")[1].strip()
        print("{0} = {0} right shift (>>) {1}".format(str1, str0), end = "")