"""
File: weather_master.py
Name: Rita Tang
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant controls when to stop
EXIT = -100


def main():
	"""
	This program will calculate the highest temperature, lowest temperature
	and average temperature among the days.
	This program will also calculate the cold days(lower than 16 degrees) among the days.
	The program will exit if the user types the exit number, here we set it as: -100
	"""
	print('stanCode \"Weather Master\" 4.0 !')
	temp = int(input('Next Temperature: (or '+str(EXIT)+' to quit)? '))
	if temp == EXIT:
		print('No temperatures were entered.')
	else:
		maximum = temp
		minimum = temp
		# to calculate total temperature
		temp_all = temp
		# to count times of temperature typing in, and include the first time
		times = 1
		# to count cold days, and include the first temperature data
		if temp < 16:
			cold_day = 1
		else:
			cold_day = 0

		while True:
			temp = int(input('Next Temperature: (or '+str(EXIT)+' to quit)? '))
			if temp == EXIT:
				break
			if temp < 16:
				cold_day += 1
			if maximum < temp:
				maximum = temp
			if minimum > temp:
				minimum = temp
			temp_all += temp
			times += 1

		# count average temperature
		avg_temp = (temp_all / times)

		print('Highest temperature = '+str(maximum))
		print('Lowest temperature = '+str(minimum))
		print('Average = ' + str(avg_temp))
		print(str(cold_day)+' cold day(s)')











###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
