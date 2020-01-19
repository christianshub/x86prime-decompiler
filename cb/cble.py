def cble(string):
    
    if "cble" in string:
        s = string.split(",")[0].split("cble")[1].strip()
        d = string.split(",")[1].strip()
        p = string.split(",")[2].strip()
        print("if {0} <= {1} (signed) then jump to {2}".format(s, d, p), end = "")    


# string = "cble %rsi, %rax, .L3"
# cble(string)