def cbge(string):
    
    if ("cbge" in string):
        s = string.split(",")[0].split("cbge")[1].strip()
        d = string.split(",")[1].strip()
        p = string.split(",")[2].strip()
        print("if {0} >= {1} (signed) then jump to {2}".format(s, d, p), end = "")    

# string = "cbge %rsi, %rax, .L3"
# cbge(string)