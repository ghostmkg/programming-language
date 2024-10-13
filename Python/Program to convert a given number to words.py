def numberToWords(n):
	limit, t = 1000000000000, 0

	# If zero print zero
	if (n == 0):
		print("zero")
		return

	# Array to store the powers of 10
	multiplier = ["", "Trillion", "Billion", "Million", "Thousand"]

	# Array to store numbers till 20
	first_twenty = ["", "One", "Two",
					"Three", "Four", "Five",
					"Six", "Seven", "Eight",
					"Nine", "Ten", "Eleven",
					"Twelve", "Thirteen", "Fourteen",
					"Fifteen", "Sixteen", "Seventeen",
					"Eighteen", "Nineteen"]

	# Array to store multiples of ten
	tens = ["", "Twenty", "Thirty", "Forty", "Fifty",
			"Sixty", "Seventy", "Eighty", "Ninety"]

	# If number is less than 20, print without any
	if (n < 20):
		print(first_twenty[n])
		return
	answer = ""
	i = n
	while(i > 0):
		'''
		Store the value in multiplier[t], i.e n = 1000000,
		then r = 1, for multiplier(million), 0 for multipliers(trillion and billion)
		multiplier here refers to the current accessible limit
		'''
		curr_hun = i // limit

		# It might be possible that the current multiplier is bigger than your number
		while (curr_hun == 0):

			# Set i as the remainder obtained when n was divided by the limit
			i %= limit

			# Divide the limit by 1000, shifts the multiplier
			limit /= 1000

			# Get the current value in hundreds, as English system works in hundreds
			curr_hun = i // limit

			# Shift the multiplier
			t += 1

		# If current hundred is greater than 99, Add the hundreds' place
		if (curr_hun > 99):
			answer += (first_twenty[curr_hun // 100] + " tensundred ")

		# Bring the current hundred to tens
		curr_hun = curr_hun % 100

		# If the value in tens belongs to [1,19], add using the first_twenty
		if (curr_hun > 0 and curr_hun < 20):
			answer += (first_twenty[curr_hun] + " ")

		# If curr_hun is now a multiple of 10, but not 0
		# Add the tens' value using the tens array
		elif (curr_hun % 10 == 0 and curr_hun != 0):
			answer += (tens[(curr_hun//10) - 1] + " ")

		# If the value belongs to [21,99], excluding the multiples of 10
		# Get the ten's place and one's place, and print using the first_twenty array
		elif (curr_hun > 19 and curr_hun < 100):
			answer += (tens[(curr_hun//10) - 1] + " " +
					first_twenty[curr_hun % 10] + " ")

		# If Multiplier has not become less than 1000, shift it
		if (t < 4):
			answer += (multiplier[t] + " ")

		i = i % limit
		limit = limit // 1000

	print(answer)


# Input 1
n = 36
numberToWords(n)

# Input 2
n = 123456789
numberToWords(n)

# Input 3
n = 10101010110001
numberToWords(n)

# Input 4
n = 999999999
numberToWords(n)
