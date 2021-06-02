# from numpy import genfromtxt
# my_data = genfromtxt('biostats.csv', delimiter=',')

import csv

reader = csv.DictReader(open('biostats.csv'))
dictobj = next(reader)
print(dictobj)
dictobj = next(reader)
print(dictobj)



with open('biostats.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		print(row)
		# print(', '.join(row))
