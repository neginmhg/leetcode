def bubble(arr):
    #get the length
    n = len(arr)
    #loop i for each passes from [0 to n-1]
    # inner loop j for swapping from [0 to n-1-i )
    #if in one round of inner loop no swap happens then that means the
    #array is sorted and we should break 

    for i in range(n):
        swapped =False
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                #swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
                #mark the flag as swapped meaning this pass was unsorted
                swapped =True
        if not swapped:
            break
    return arr



res=bubble([5,3,8,4,2])
print(res)