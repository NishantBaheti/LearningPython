import prime

from time import time

def print_prime_number(last):
    
    digit = 2
    while digit <= last :

        is_prime = True
        cursor = 2
        while cursor <= digit/2:
            
            if digit % cursor == 0:
                is_prime = False
                break

            cursor += 1

            
        if is_prime:
            print(digit)

        digit += 1



if __name__ == "__main__":

    start = time()
    # print_prime_number(100000)  # time taken : 73.944256067276
    prime.print_prime_number(100000)  # time taken : 2.504993200302124

    end = time()

    print("time taken :",end-start)
