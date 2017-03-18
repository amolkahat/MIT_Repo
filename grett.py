def check_number(number):
	if number % 2 == 0 :
		return True
	else:
	   return False

# Do square of a number
def squr(number):
	if check_number(number):
		return number ** 2

print(squr(100))
