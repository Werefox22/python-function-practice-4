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