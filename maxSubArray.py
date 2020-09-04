#this program will be nice
import math

def find_max_subarray(A, low, mid, high):
    left_sum = float("-inf")
    sum = 0
    for i in range(mid, low, -1):
        print(A[i])
        sum = sum + A[i]
        if (sum > left_sum):
            left_sum = sum
            max_left = i
    right_sum = float("-inf")
    sum = 0
    for j in range(mid+1, high):
        print(j)
        sum = sum + A[j]
        if (sum > right_sum):
            right_sum = sum
            max_right = j
    print(left_sum)
    print(right_sum)
    return (max_left, max_right, left_sum + right_sum)

table = [ i for i in range(10)]
print(find_max_subarray(table,0,5,10))
