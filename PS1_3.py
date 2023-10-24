def Pascal_triangle(k):
    l1 = ([[1],[1,1]])
    n = 3
    while n <= k:
        for i in range(0,n-1):
            if i == 0:
                l1.append([1,1])
            else:
                l1[n-1].insert(i,l1[n-2][i]+l1[n-2][i-1])
                #Look it up on the online and extract the corresponding number from the nested array in the list
        n = n + 1
    else:
        print(l1[k-1])
Pascal_triangle(100)
Pascal_triangle(200)