def cbg(string):
    
    if ("cbg" in string) and not ("cbge" in string):
        s = string.split(",")[0].split("cbg")[1].strip()
        d = string.split(",")[1].strip()
        p = string.split(",")[2].strip()
        print("if {0} > {1} (signed) then jump to {2}".format(s, d, p), end = "")    

# string = "cbg %rsi, %rax, .L3"
# cbg(string)