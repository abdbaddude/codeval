#!/usr/bin/env python3
"""
Our marketing department has just negotiated a deal with several local merchants that will
allow us to offer exclusive discounts on various products to our top customers every day. 
The catch is that we can only offer each product to one customer and we may only offer 
one product to each customer.

Each day we will get the list of products that are eligible for these special discounts. 
We then have to decide which products to offer to which of our customers. 
Fortunately, our team of highly skilled statisticians has developed an amazing mathematical 
model for determining how likely a given customer is to buy an offered product by 
calculating what we call the "suitability score" (SS). 
The top-secret algorithm to calculate the SS between a customer and a product is this: 

1. If the number of letters in the product's name is even then the SS is the number of 
   vowels (a, e, i, o, u, y) in the customer's name multiplied by 1.5. 
2. If the number of letters in the product's name is odd then the SS is the number of 
   consonants in the customer's name. 
3. If the number of letters in the product's name shares any common factors (besides 1) 
   with the number of letters in the customer's name then the SS is multiplied by 1.5. 

Your task is to implement a program that assigns each customer a product to be offered in 
a way that maximizes the combined total SS across all of the chosen offers. 
Note that there may be a different number of products and customers. 
You may include code from external libraries as long as you cite the source.

INPUT SAMPLE:

Your program should accept as its only argument a path to a file. 
Each line in this file is one test case. 
Each test case will be a comma delimited set of customer names followed by a semicolon and
 then a comma delimited set of product names. 
Assume the input file is ASCII encoded. 
For example (NOTE: The example below has 3 test cases): 

Jack Abraham,John Evans,Ted Dziuba;iPad 2 - 4-pack,Girl Scouts Thin Mints,Nerf Crossbow
Jeffery Lebowski,Walter Sobchak,Theodore Donald Kerabatsos,Peter Gibbons,Michael Bolton,Samir Nagheenanajar;Half & Half,Colt M1911A1,16lb bowling ball,Red Swingline Stapler,Printer paper,Vibe Magazine Subscriptions - 40 pack
Jareau Wade,Rob Eroh,Mahmoud Abdelkader,Wenyi Cai,Justin Van Winkle,Gabriel Sinkin,Aaron Adelson;Batman No. 1,Football - Official Size,Bass Amplifying Headphones,Elephant food - 1024 lbs,Three Wolf One Moon T-shirt,Dom Perignon 2000 Vintage

OUTPUT SAMPLE:

For each line of input, print out the maximum total score to two decimal places. 
For the example input above, the output should look like this:

21.00
83.50
71.25
"""


def name_letters_only(name):
	"""
	Retain only letters in a name
	"""
	letters='abcdefghijklmnopqrstuvwxyz'
	name=name.lower()
	return [i for i in name if i in letters]


def gcd(x,y):
	"""
	Euclideans algorithm to get Greatest Common Denominator
	"""
	if x == y : return x
	if x > y : 
		return gcd(x-y,y)
	else:
		return gcd(x,y-x)
		 
def even_or_odd_product_name_SS(product_name,customers_name): 
	"""
	1. If the number of letters in the product's name is even then the SS is the number of 
	   vowels (a, e, i, o, u, y) in the customer's name multiplied by 1.5. 
	2. If the number of letters in the product's name is odd then the SS is the number of 
	   consonants in the customer's name. 
	3. If the number of letters in the product's name shares any common factors (besides 1) 
	   with the number of letters in the customer's name then the SS is multiplied by 1.5. 
	"""
	product_name = name_letters_only(product_name)       #only letters considered
	customers_name = name_letters_only(customers_name)   #only letters considered
	vowels = ('a', 'e', 'i', 'o', 'u', 'y')
	number_of_vowels_customer = 0
	customers_name_length = len(customers_name)
	product_name_length = len(product_name)
	for i in vowels:
			number_of_vowels_customer = number_of_vowels_customer + customers_name.count(i)		
	total_SS = (customers_name_length - number_of_vowels_customer) if product_name_length & 1 == 1 else number_of_vowels_customer * 1.5	
	return total_SS * ( 1.5 if gcd(product_name_length,customers_name_length) != 1 else 1.0)
	
def discount_offers(line):
	customers=line.split(";")[0].split(",")
	products=line.split(";")[1].split(",")
	max_offer = {}
	
	for customer in customers: 
		customer_possible_discount_offers = dict()
		for product in products:
			customer_possible_discount_offers[product] = even_or_odd_product_name_SS(product,customer)
		print("{}".format(customer_possible_discount_offers.values()))
		max_customer_discount_offer = max(zip(customer_possible_discount_offers.values(), customer_possible_discount_offers.keys()))
		max_offer[customer] = max_customer_discount_offer		


if __name__ == '__main__':
	import sys
	test_cases = open(sys.argv[1], 'r')	
	tests=test_cases.readlines()
	test_case = 0
	MAX_TEST_CASE_NBR=40	
	try:
		for test in tests:		 
				''' The 40 TC constraint'''		
				if (test_case == MAX_TEST_CASE_NBR):
						break
				if test.strip(): #only nonempty lines are considered
					discount_offers(test.strip())
				test_case += 1	
		EXIT_CODE = 0
	except:
		EXIT_CODE = -1	
	sys.exit(EXIT_CODE)	
	
	
"""
[
[13.5, 9.0, 9.0, 9.0,13.5, 9.0],
[ 6.0, 9.0, 9.0,13.5, 6.0, 6.0],
[22.5,14.0,14.0,14.0,22.5,22.5],
[ 9.0, 8.0, 8.0, 8.0, 9.0, 9.0],
[ 7.5, 8.0, 8.0,12.0, 7.5, 7.5],
[18.0,10.0,10.0,10.0,18.0,18.0]
]
"""
		
	


	
