def max_sub_array(A):
    max_sum = A[0]
    for i in range(0, len(A)):
        sum = 0
        for j in range(i, len(A)):
            sum += A[j]
            max_sum = max(max_sum, sum)

    return max_sum

print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))
