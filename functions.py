# max_num
def max_num(x, y, z):
	return max((x, y, z))

print("max_num tests:")
print(max_num(1, 0, 2))
print(max_num(10, 12, 13))
print(max_num(1, -12, 0))

def mult_list(list):
	if len(list) < 1:
		return list
	elif len(list) == 1:
		return list[0]
	else:
		list[-1] *= list[0]
		return mult_list(list[1:])

print("\nmult_list tests:")
print(mult_list([1, 2, 3]))
print(mult_list([10, -10]))
print(mult_list([-1, 1, 1, 1, 1, 1, -1]))
print(mult_list([]))
print(mult_list([1000, -2000, -3000, 4000]))
print(mult_list([1000000, 1000000, 0]))

def rev_string(string):
	return string[::-1]

print("\nrev_string tests:")
print(rev_string("string"))
print(rev_string("Panama"))
print(rev_string("Hello, world!"))

def num_within(num, start, end):
	return num >= start and num <= end

print("\nnum_within tests:")
print(num_within(1, 0, 10)) 	# True
print(num_within(10, 1, 10))	# True
print(num_within(10, 10, 11))	# True
print(num_within(10, 11, 100))	# False
print(num_within(1.5, 0, 3))	# True
print(num_within(3.1, 0, 3))	# False
print(num_within(-5, 1, 10))	# False
print(num_within(-5, -1, 10))	# False
print(num_within(-5, -10, 1))	# True
print(num_within(5, 10, 1))		# False (While 5 is inbetween 1 and 10, the start and end are switched)
print(num_within(10, 8, 2))		# False (Start and end are switched again)

# diagram:
# pascal(3)
#	get third row -> pascal(2)

def pascal(n):
	if n == 1:
		print([1])
		return [1, 1]
	else:
		row = pascal(n - 1)
		print(row)
		next_row = [1, 1]
		for i in range(1, len(row)):
			next_row.insert(1, row[i - 1] + row[i])
		return next_row


print("\npascal tests:")
pascal(1)
pascal(3)
pascal(10)