array = [ 2, 24, 45, 66, 75, 90, 170, 802 ]
find_element = 802

def binary_search ( array , size_correction) :
    mid_element = int( ( 0 + len(array) )/2 )
    
    if array [ mid_element ] == find_element : 
        return ( size_correction + mid_element )
        
    elif array [ mid_element ] > find_element : 
        return binary_search ( array [ : mid_element ] ,  size_correction )
        
    elif array [ mid_element ] < find_element : 
        return binary_search ( array [ mid_element + 1 : ] , ( size_correction + mid_element + 1 ) )
        
    else : return -1
    
# gives index
print ( binary_search ( array , 0 ) )