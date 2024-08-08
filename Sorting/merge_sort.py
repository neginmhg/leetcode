def mergeSort(arr):
    #recurssion base case
    if len(arr) >1:
        #find middle
        mid =len(arr) //2
        #split into 2 lists based on middle
        leftHalf = arr[:mid]
        rightHalf = arr[mid:]
        #call recusrrion of each list
        mergeSort(leftHalf)
        mergeSort(rightHalf)
        #copmarison logic with pointer from i for leftlist, j for rightlist, and k for resullist
        i=j=k=0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                arr[k] = leftHalf[i]
                i +=1
            else:
                arr[k] = rightHalf[j]
                j+=1
            k +=1
        


        #copy remaining of left side, if any
        while i < len(leftHalf):
            arr[k] = leftHalf[i]
            i += 1
            k += 1

        # Copy remaining elements from rightHalf, if any
        while j < len(rightHalf):
            arr[k] = rightHalf[j]
            j += 1
            k += 1
    return arr


res=mergeSort([27, 38, 43,3, 9, 10, 82])
print(res)