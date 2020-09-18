def georgeCantor(n): 
    i = 1 
    j = 1
    k = 1
    while k < n: 
        j += 1
        k += 1
        if k == n: 
            break
        # loop for traversing from right 
        # to left downwards diagonally 
        while j > 1 and k < n: 
            i += 1
            j -= 1
            k += 1
        if k == n: 
            break
        i += 1
        k += 1
        if k == n: 
            break
        # loop for traversing from left 
        # to right upwards diagonally 
        while i > 1 and k < n: 
            i -= 1
            j += 1
            k += 1
    #print ("N-th term : %d/%d"%(i, j)) 
    print("TERM {} IS {}/{}".format(n, i, j))
while True:
    try:
        n = int(input())
        georgeCantor(n)
    except EOFError:
        break
