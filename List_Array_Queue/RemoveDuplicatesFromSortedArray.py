A = [1,1,3]
def removeDuplicatesI(sortedArray):
    index = 0
    for i in range(len(sortedArray)):
        if sortedArray[index] != sortedArray[i]:
            index +=1
            sortedArray[index] = sortedArray[i]
    return index+1

B=[1,1,1,2,2,2,3,3,3]
def removeDuplicatesII(sortedArray,nums):
    index = nums
    for i in range(nums,len(sortedArray)):
        if sortedArray[index-nums] != sortedArray[i]:
            index +=1
            sortedArray[index-1] = sortedArray[i]
    return index

if __name__ == "__main__":
    lengthArrayI = removeDuplicatesI(A)
    print(lengthArrayI)

    lengthArrayII = removeDuplicatesII(B,2)
    print(lengthArrayII)