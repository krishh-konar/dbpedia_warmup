#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string 
arabic_to_english = {
	'٠': '0', '١': '1',	'٢': '2', '٣': '3',	'٤': '4',
	'٥': '5', '٦': '6',	'٧': '7', '٨': '8',	'٩': '9', ',':'', '.':''
}

eng_to_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           		(50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def translateArabicToEng(num):
	#num = num.decode('utf-8')
	#d = unicode(num, 'utf-8')
	if num.isnumeric(): return num
	#num = num.encode('utf-8')
	eng_num = ""
	for z in num:
		n = z.encode('utf-8')
		eng_num += arabic_to_english[n]

	try: return int(eng_num)
	except:
		print 'Invalid input'
		return 

def translate(num):
	num = int(translateArabicToEng(num))
	n = num
	roman = ''
	while num > 0:
		for i, r in eng_to_roman:
			while num >= i:
				roman += r
				num -= i
	return [n, roman]

def parseQuery(query):
	tokens = (string.lower(query)).decode('utf-8').split()
	target = []

	if 'translate' in tokens:
		for t in tokens:
			z = t[0].encode('utf-8')
			if t[0].isdigit():
				target.append(t)
			if z in arabic_to_english:
				target.append(t)
	
	if len(target)>0:
		for num in target:
			x = translate(num)
			print num, ": (", x[0], ") ",x[1]
	else:
		print 'Query not recognised. Try again.'


def main():
	print 'Enter your query(Use "translate <num>" for translation, "exit" to terminate)\n\n>> ',
	s = raw_input()
	while True:
		if s == "exit": break
		parseQuery(s)
		print "\n>> ",
		s = raw_input().strip()

if __name__ == '__main__':
	main()