def sum(n):
	sum = 0
	fact = 1

	for i in range(1, n + 1):
		fact *= i
		sum += 1.0/fact

	print(sum)
n = 1
sum(n)
