def unique(s):
    st = ""
    length = len(s)
    for i in range(length):
        c = s[i]
        if c not in st:
            st+=c
    return st
            
