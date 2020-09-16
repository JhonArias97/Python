def xo(s):
    s = str.lower(s)
    nx = 0
    no = 0
    for n in s:
        if n == "x":
            nx += 1
        elif n == "o":
            no += 1
        else:
            continue
    if nx == no:
        return True
    else:
        return False