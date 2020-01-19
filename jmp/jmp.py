def jmp(string):
    if "jmp" in string:
        str0 = string.split(" ")[0].strip()
        str1 = string.split(" ")[1].strip()
        print("{0} to {1}".format(str0, str1), end = "")    
