# Python3 implementation to convert a binary number 
# to octal number 

# function to create map between binary 
# number and its equivalent octal 
def createMap(bin_oct_map): 
	bin_oct_map["000"] = '0'
	bin_oct_map["001"] = '1'
	bin_oct_map["010"] = '2'
	bin_oct_map["011"] = '3'
	bin_oct_map["100"] = '4'
	bin_oct_map["101"] = '5'
	bin_oct_map["110"] = '6'
	bin_oct_map["111"] = '7'

# Function to find octal equivalent of binary 
def convertBinToOct(bin): 
	l = len(bin) 
	
	# length of string before '.' 
	t = -1
	if '.' in bin: 
		t = bin.index('.') 
		len_left = t 
	else: 
		len_left = l 
	
	# add min 0's in the beginning to make 
	# left substring length divisible by 3 
	for i in range(1, (3 - len_left % 3) % 3 + 1): 
		bin = '0' + bin
	
	# if decimal point exists 
	if (t != -1): 
		
		# length of string after '.' 
		len_right = l - len_left - 1
		
		# add min 0's in the end to make right 
		# substring length divisible by 3 
		for i in range(1, (3 - len_right % 3) % 3 + 1): 
			bin = bin + '0'
	
	# create dictionary between binary and its 
	# equivalent octal code 
	bin_oct_map = {} 
	createMap(bin_oct_map) 
	i = 0
	octal = "" 
	
	while (True) : 
		
		# one by one extract from left, substring 
		# of size 3 and add its octal code 
		octal += bin_oct_map[bin[i:i + 3]] 
		i += 3
		if (i == len(bin)): 
			break
			
		# if '.' is encountered add it to result 
		if (bin[i] == '.'): 
			octal += '.'
			i += 1
			
	# required octal number 
	return octal 

# Driver Code 
bin = "1111001010010100001.010110110011011"
print("Octal number = ", 
	convertBinToOct(bin)) 
