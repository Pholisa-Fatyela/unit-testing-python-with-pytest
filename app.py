
import calc
import sys

while True:
	calc_string = input ("Please enter a calculation: ")

	if calc_string == "q":
		print ("bye!")
		break
	parts = calc_string.split(" ")
	
	if len(parts) == 3 :
		num1 = int(parts[0])
		operator = parts[1]
		num2 = int(parts[2])

		try:
			
			result = calc.execute(num1, num2, operator)
			print (result)

		except:
			print(sys.exc_info()[0])
	else:
		print("Invalid argument. Type something like '8 - 3'. ")
