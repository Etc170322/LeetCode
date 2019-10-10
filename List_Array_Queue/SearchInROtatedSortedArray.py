A = [4,5,6,7,0,1,2]

def searchI(rotatedSortedArray,value):
    first = 0;last = len(rotatedSortedArray)
    while first!=last:
        mid = first + (last-first)//2
        if rotatedSortedArray[mid] == value:
            return mid
        if rotatedSortedArray[first]<rotatedSortedArray[mid]:
            if rotatedSortedArray[first]<=value and rotatedSortedArray[mid]>value:
                last = mid
            else:
                first = mid+1
        else:
            if rotatedSortedArray[mid] <value and rotatedSortedArray[last-1] <= value:
                first = mid +1
            else:
                last = mid
    return -1

B = [3,4,4,4,5,6,1,1,2,3,3]
def searchII(rotatedSortedDuplicatedArray,value):
    first = 0;last = len(rotatedSortedDuplicatedArray)
    while first != last:
        mid = first + (last - first)//2
        if rotatedSortedDuplicatedArray[mid] == value:
            return mid
        if rotatedSortedDuplicatedArray[first] < rotatedSortedDuplicatedArray[mid]:
            if rotatedSortedDuplicatedArray[first]<=value and rotatedSortedDuplicatedArray[mid] > value:
                last = mid
            else:
                first = mid+1
        elif rotatedSortedDuplicatedArray[first] > rotatedSortedDuplicatedArray[mid]:
            if rotatedSortedDuplicatedArray[mid] < value and rotatedSortedDuplicatedArray[last -1]:
                first = mid+1
            else:
                last = mid
        else:
            first += 1
    return -1

if __name__ == "__main__":
    indexI = searchI(A,5)
    print(indexI)
    indexII = searchII(B,5)
    print(indexII)

