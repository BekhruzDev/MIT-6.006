def count_long_subarray_v1(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    
    number_of_subarrays = 0
    subarray_size = 0
    subarrays_dict = {}
    array_size = len(A)
    
    for i in range(array_size - 1):
        x = A[i]
        y = A[i + 1]
        if y>x:
            subarray_size += 1   
            if y == A[array_size-1]:
                number_of_subarrays += 1
                if subarrays_dict.get(subarray_size) == None:
                    subarrays_dict[subarray_size] = number_of_subarrays
                else:
                    subarrays_dict[subarray_size] += number_of_subarrays
                subarray_size = 0
                number_of_subarrays = 0
        else: 
            if subarray_size >= 1 :
                number_of_subarrays += 1
                if subarrays_dict.get(subarray_size) == None:
                    subarrays_dict[subarray_size] = number_of_subarrays
                else:
                    subarrays_dict[subarray_size] += number_of_subarrays
                subarray_size = 0
                number_of_subarrays = 0

    
    max_elements = 0
    for pair in subarrays_dict.keys():
        if max_elements < pair:
            max_elements = pair
        
                
      
    print(subarrays_dict)   
    return subarrays_dict[max_elements]



def count_long_subarray(A):
    n = len(A)
    current_long_size = 1
    long_size = 1
    count = 1
    
    for i in range(n - 1):
        if A[i] < A[i + 1]:
            current_long_size += 1
        else: 
            current_long_size = 1
        if current_long_size == long_size:
            count += 1
        elif current_long_size > long_size:
            long_size = current_long_size
            count = 1
        
    return count
            
            



#TEST
t = (2, 2, 4, 1, 4)
print(count_long_subarray(t))

