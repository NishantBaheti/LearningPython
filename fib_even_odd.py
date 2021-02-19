

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
