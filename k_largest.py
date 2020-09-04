def k_Largest(A,k):
    #make a new array of length k
    B = [0] * k
    #populate new array with 0's
    for i in range(0,k):
        B[i] = 0
    #loop for A array
    sumI = 0
    sumW = 0
    for i in range(0, len(A)):
        if A[i] > B[0]:
            sumI = sumI + 1
            B[0] = A[i]
            j = 1
            #sjekker om B sitt neste element er større enn det forrige
            while (j < len(B) and B[j-1] > B[j]):
                sumW = sumW + 1
                B[j-1], B[j] = B[j], B[j-1]
                j = j + 1
    sum = 0
    for i in range(0,k):
        sum = sum + B[i]
    print("if check ran " +str(sumI) + "times")
    print("Wile loop ran " +str(sumW) + "times")
    return sum
