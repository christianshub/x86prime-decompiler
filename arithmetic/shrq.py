def shrq(string):
    if ("shrq" in string):
        str0 = string.split(",")[0].strip().split("shrq")[1].strip()
        str1 = string.split(",")[1].strip()
        print("{0} = {0} right shift logical (>>) {1}".format(str1, str0), end = "")