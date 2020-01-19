def mov(string):
    if "movq" in string:
        str0 = string.split(",")[0].strip().split("movq")[1].strip()
        str1 = string.split(",")[1].strip()
        print("{0} = {1}".format(str1, str0), end = "")    
