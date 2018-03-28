def cidr_to_binary(cidr):
    k = []
    st = ""
    cidr = int(cidr)
    for i in range(cidr):
        k.append(1)
    for i in range(cidr,32):
        k.append(0)
    j = 0
    for i in k:
        j += 1
        if j > 8:
            st = st + " "
            j = 1
        st = st + str(i)
    return st