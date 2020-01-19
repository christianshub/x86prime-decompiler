def label(string):
    if (".L" in string) and (":" in string):
        print(string.strip(), end = "")
        print("\n")
        print("====", string.strip(), "=============================================================", end = "")     
