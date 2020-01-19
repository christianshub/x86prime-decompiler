def cba(string):
    
    if ("cba" in string) and not ("cbae" in string):
        s = string.split(",")[0].split("cba")[1].strip()
        d = string.split(",")[1].strip()
        p = string.split(",")[2].strip()
        print("if {0} > {1} (unsigned) then jump to {2}".format(s, d, p), end = "")    

# string = "cba %rsi, %rax, .L3"
# cba(string)