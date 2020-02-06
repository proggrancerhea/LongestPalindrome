import numpy as np
import math
import pdb
#def palindrome(string):
#12
def palindrome(string):
    n = len(string)
#pdb.set_trace()
    check = np.zeros((n,n), dtype=bool)
#print check
    max_length = 0
    for i in range(n):
            check[i][i] = True
            max_length = 1
            startindex = i
    for i in range(n-1):
        if string[i] == string[i+1]:
            check[i][i+1] = True
            max_length = 2
            startindex = i
    for k in range(3, n):
        for i in range(n-k+1):
            j = i +k -1
            if check[i+1][j-1] and string[i] == string[j]:
                check[i][j] = True
                if k>max_length:
                    max_length = k
                    startindex = i
    return string[startindex: startindex+max_length]
print palindrome('pouhhhhgfdhh')