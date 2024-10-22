def print_prime_number_cython(int last):
    
    cdef int digit,is_prime,cursor
    
    digit = 2
    while digit <= last :

        is_prime = 1
        cursor = 2
        while cursor <= digit/2:
            
            if digit % cursor == 0:
                is_prime = 0
                break

            cursor += 1

            
        # if is_prime:
        #     print(digit)

        digit += 1