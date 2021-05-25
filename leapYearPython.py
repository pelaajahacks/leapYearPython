first_leap = 2020
yearInput = int(input("Year: "))
year = yearInput

while True:
	if year == first_leap:
		print(str(yearInput), "Is a leap year")
		break
	elif year < first_leap:
		year += 4
		if year == first_leap:
			print(str(yearInput), "Is a leap year!")
			break
	elif year > first_leap:
		year -= 4
		if year == first_leap:
			print(str(yearInput), "Is a leap year!")
			break
	else:
		print("An error occured, please try again")
		break
