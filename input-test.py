#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fractions import gcd

def get_input(question):
	converted_answer = 0
	while not converted_answer:
		user_answer = raw_input(question + ' ')
		converted_answer = convert_answer(user_answer)
	return converted_answer

def convert_answer(user_input):
	string_space = ' '
	string_fraction = '/'
	float_calculation = 0
	float_whole = 0
	float_numerator = 0
	float_denominator = 1
	try:
		user_input = user_input.lstrip()
		if user_input.isdigit():
			float_whole = float(user_input)
		else:
			#~ while user_input[0] is string_space:
				#~ user_input = user_input[1:]
			if user_input.find(string_space) is not -1:
				end_of_whole_number = user_input.find(string_space)
				float_whole = float(user_input[:end_of_whole_number])
				while user_input[0] is not string_space:
					user_input = user_input[1:]
			divisor = user_input.find(string_fraction)
			float_numerator = float(user_input[:divisor])
			float_denominator = float(user_input[divisor + 1:])
		float_calculation = float_calculation + float_whole
		float_calculation += float_numerator / float_denominator
	except StandardError:
		print('Your response is not recognized.')
	return float_calculation

def float_to_fraction(float_from_user):
	str_test = str(float_from_user)
	int_decimal_point = str_test.find('.')
	str_whole = str_test[:int_decimal_point]
	str_decimal = str_test[int_decimal_point:] #includes decimal point
	int_numerator = int(str_decimal[1:])
	int_decimal_places = len(str_decimal[1:])
	int_denominator = 10**int_decimal_places
	int_divisor = gcd(int_numerator, int_denominator)
	str_reduced_numerator = str(int_numerator / int_divisor)
	str_reduced_denominator = str(int_denominator / int_divisor)
	str_mixed_number = (str_whole + ' ' + str_reduced_numerator + '/' + 
		str_reduced_denominator)
	return str_mixed_number

def main():
	float_picture_height = get_input('Picture height:')
	print(float_picture_height)
	print(float_to_fraction(float_picture_height))
	float_frame_height = get_input('Frame height:')
	print(float_frame_height)
	print(float_to_fraction(float_frame_height))
	print('The difference between picture and frame height is: ' +
		float_to_fraction(float_frame_height - float_picture_height))
	return 0

if __name__ == '__main__':
	main()
