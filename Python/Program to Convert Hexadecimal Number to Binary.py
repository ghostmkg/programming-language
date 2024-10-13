# Python3 program to convert
# Hexadecimal number to Binary

# Function to convert
# Hexadecimal to Binary Number
def HexToBin(hexdec):

	for i in hexdec:	 
		if i == '0':
			print('0000', end = '')
		elif i == '1':
			print('0001', end = '')
		elif i == '2':
			print('0010', end = '')
		elif i == '3':
			print('0011', end = '')
		elif i == '4':
			print('0100', end = '')
		elif i == '5':
			print('0101', end = '')
		elif i == '6':
			print('0110', end = '')
		elif i == '7':
			print('0111', end = '')
		elif i == '8':
			print('1000', end = '')
		elif i == '9':
			print('1001', end = '')
		elif i == 'A' or i == 'a':
			print('1010', end = '')
		elif i == 'B' or i == 'b':
			print('1011', end = '')
		elif i == 'C' or i == 'c':
			print('1100', end = '')
		elif i == 'D' or i == 'd':
			print('1101', end = '')
		elif i == 'E' or i == 'e':
			print('1110', end = '')
		elif i == 'F' or i == 'f':
			print('1111', end = '')
		elif i == '.':
			print('.', end = '')
		else:
			print("\nInvalid hexadecimal digit " +
					str(hexdec[i]), end = '')
			
# Driver code
if __name__=="__main__":
	
	# Get the Hexadecimal number
	hexdec= "1AC5";

	# Convert HexaDecimal to Binary
	print("Equivalent Binary value is : ",
		end = '')
	HexToBin(hexdec)
	
# This code is contributed by baliraje_kalyane
