def leaq(string):
    if ("leaq" in string):
        count = string.count(",")
        
        # if 3 kommas in leaq
        if (count is 3):
            i = string.split(",")[0].split("leaq")[1].split("(")[0].strip()
            s = string.split(",")[0].split("leaq")[1].split("(")[1].strip()
            z = string.split(",")[1].strip()
            v = string.split(",")[2].split(")")[0].strip()
            d = string.split(",")[3].strip()
            
            print("{0} + {1} + ({2} * {3}) -> {4}".format(i, s, z, v, d), end = "")

        if (count is 1):
            # leaq (s),d or leaq i(s),d
            if ("(") in string:  
                if (string.split("(")[0].split("leaq")[1].strip() is not ""):
                    # leaq i(s),d
                    i = string.split(",")[0].split("(")[0].split("leaq")[1].strip()
                    s = string.split(",")[0].split("(")[1].strip()
                    d = string.split(",")[1].strip()
                    print("{0} + ({1} -> {2} (Add a constant)".format(i, s, d), end = "")

                else:
                    # leaq (s),d
                    s = string.split(",")[0].split("leaq")[1].strip()
                    d = string.split(",")[1].strip()
                    print("{0} -> {1} (Copy value from register s to register d)".format(s, d), end = "")
            else:
            #leaq i,d
                i = string.split(",")[0].split("leaq")[1].strip()
                d = string.split(",")[1].strip()
                print("{0} -> {1} (get a constant)".format(i, d), end = "")


# leaq("leaq 5(%rsi), %r11")
# print("")
# leaq("leaq (%rsi), %r11")