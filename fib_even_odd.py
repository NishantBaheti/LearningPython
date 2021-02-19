"""
Display sequence of Fibonacci series until the number given by user and count total even numbers and odd numbers in that series except zero. Fibonacci series should start with 1. Total count of even numbers should be displayed in the first row and odd numbers should be displayed in the next row.Number given by user for Fibonacci series should be greater than 5 and less than or equal to 20 otherwise display "INVALID INPUT".If the number given by the user is space, character or empty display “INVALIDOUTPUT”.
"""

def fib_series(n):
	l = [1,1]
	i = 2
	odd_count = 2
	even_count = 0
	while i< n:
		new = l[-1] + l[-2]
		l.append(new)
		if new % 2 == 0:
			even_count += 1
		else:
			odd_count += 1
		i+=1
	return l,odd_count,even_count


if __name__ == "__main__":
	n = int(input())
	if n in range(6,21):
		print(fib_series(n)) 
	else:
		print("INVALID INPUT")	
