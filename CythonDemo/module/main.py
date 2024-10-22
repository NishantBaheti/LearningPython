from prime import print_prime_number_cython

from time import time

def timeit(func):
    def inner(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"function : {func.__name__} | time taken : {end-start}")
        return result
    return inner


def print_prime_number_python(last):
    
    digit = 2
    while digit <= last :

        is_prime = True
        cursor = 2
        while cursor <= digit/2:
            
            if digit % cursor == 0:
                is_prime = False
                break

            cursor += 1
            
        # if is_prime:
        #     print(digit)

        digit += 1



if __name__ == "__main__":
    # python setup.py build_ext --inplace

    timeit(print_prime_number_python)(100000)  # time taken : 73.944256067276
    
    timeit(print_prime_number_cython)(100000)  # time taken : 2.504993200302124
