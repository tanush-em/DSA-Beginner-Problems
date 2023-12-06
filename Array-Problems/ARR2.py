# MAXIMUM AND MINIMUM ELEMNTS IN AN ARRAY

def MinMax(low,high,arr):
    arr_min = arr_min = arr[low]
    
    # Basecase 1 : Only 1 element is present
    if low == high:
        arr_max = arr_min = arr[low]
        return (arr_max, arr_min)
    
    # Basecase 2 : Only 2 elements are present
    elif high == low + 1:
        if arr[high] >= arr[low]:
             arr_max = arr[high]
             arr_min = arr[low]
        else:
            arr_max = arr[low]
            arr_min = arr[high]
        return(arr_max, arr_min)
    
    # Basecase 3 : More than 2 elements are present
    else:
        mid = int((high+low)/2)
        arr_max1, arr_min1 = MinMax(low, mid, arr)
        arr_max2, arr_min2 = MinMax(mid+1,high,arr)
        
        arr_max = max(arr_max1, arr_max2)
        arr_min = min(arr_min1, arr_min2)
        return (arr_max, arr_min)