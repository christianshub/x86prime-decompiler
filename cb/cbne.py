def cbne(string):
    
    if ("cbne" in string):
        s = string.split(",")[0].split("cbne")[1].strip()
        d = string.split(",")[1].strip()
        p = string.split(",")[2].strip()
        print("if {0} != {1} then jump to {2}".format(s, d, p), end = "")    

# string = "cbne %rsi, %rax, .L3"
# cbne(string)