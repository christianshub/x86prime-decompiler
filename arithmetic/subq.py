def subq(string):
    if "subq" in string:
        str0 = string.split(",")[0].strip().split("subq")[1].strip()
        str1 = string.split(",")[1].strip()
        print("{0} = {0} minus (-) {1}".format(str1, str0), end = "")