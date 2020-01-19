def call(string):
    if ("call" in string):
        p = string.split(",")[0].split("call")[1].strip()
        d = string.split(",")[1].strip()
        print("calling {0}, and storing return address in {1}".format(p, d), end = "")

# string = "call allocate, %r11"
# call(string)