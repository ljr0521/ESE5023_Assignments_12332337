def Find_expression(n):
    str = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    sym = ["+", "-", ""]
    sum_n = []
    for a in sym:
        for b in sym:
            for c in sym:
                for d in sym:
                    for e in sym:
                        for f in sym:
                            for g in sym:
                                for h in sym:
                                    sum = str[0] + a + str[1] + b + str[2] + c + str[3] + d + str[4] + e + str[5] + f + \
                                          str[6] + g + str[7] + h + str[8]
                                    if eval(sum) == n:
                                        print(sum + "=", end = '')
                                        print(n)
    return sum_n
Find_expression(50)
#This question was written by my classmate Xu Jiwen with her help.
# I did not complete the second question, and I will ask others later