A = [1,2,4,6,7,8,9]
B = [2,3,5,7,9,20,11]

def findMedianSortedArrays(sortedArray_A,sortedArray_B,k):
    m = len(sortedArray_A)
    n = len(sortedArray_B)
    if k > (m + n):
        return -1
    while k != 0:
        if m == 0:
            return sortedArray_B[k-1]
        elif n == 0:
            return sortedArray_A[k-1]
        if k == 1:
            return min(sortedArray_A[0],sortedArray_B[0])
        mid = k // 2
        midIndex_A = min(mid-1, m-1)
        midIndex_B = min(mid-1, n-1)
        midIndex = min(midIndex_A,midIndex_B)
        midValue_A = sortedArray_A[midIndex]
        midValue_B = sortedArray_B[midIndex]
        if midValue_A < midValue_B:
            sortedArray_A,m,k = transferArray(sortedArray_A,midIndex_A,k)
        elif midValue_A > midValue_B:
            sortedArray_B,m,k = transferArray(sortedArray_B,midIndex_B,k)
        elif midValue_A == midValue_B:
            if midIndex_A < midIndex_B:
                sortedArray_A,m,k = transferArray(sortedArray_A,midIndex_A,k)
            elif midIndex_A > midIndex_B:
                sortedArray_B,m,k = transferArray(sortedArray_B,midIndex_B,k)
            else:
                return midValue_A

def transferArray(sortedArray,midIndex,k):
    sortedArray = sortedArray[midIndex+1:]
    m = len(sortedArray)
    k -= midIndex+1
    return sortedArray,m,k

if __name__ == "__main__":
    value = findMedianSortedArrays(A,B,10)
    print(value)