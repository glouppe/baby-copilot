def sqrt(n):
	x = n	
	y = 1	
	error = 0.001
	while (x - y > error):	
		x = (x + y) / 2		
		y = n / (x-1)			
	return (x)

print(sqrt(2))
print(sqrt(3))
print(sqrt(4))
print(sqrt(5))
