def cbl(string):
    
    if ("cbl" in string) and not ("cble" in string):
        s = string.split(",")[0].split("cbl")[1].strip()
        d = string.split(",")[1].strip()
        p = string.split(",")[2].strip()
        print("if {0} < {1} (signed) then jump to {2}".format(s, d, p), end = "")    

# string = "cbl %rsi, %rax, .L3"
# cbl(string)