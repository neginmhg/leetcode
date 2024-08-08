def quickSort(arr):
    #base case based on size of array
    if len(arr) <=1:
        return arr
    else:
        #find pivot, initilze left and right []
        pivot =arr[-1]
        left =[]  
        right =[]
        #partition into 2 based on pivot
        for i in range(len(arr)-1):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        
        #return and call recursively
        return quickSort(left) + [pivot] + quickSort(right)



res = quickSort([27, 38, 43,3, 9, 10, 82])
print(res)