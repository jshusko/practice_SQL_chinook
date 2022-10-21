# -*- coding: utf-8 -*-i

"""
Test sqlite Python against sqlite raw queries from LucasMcl
October 6, 2022
"""

__author__ = 'Jacob Shusko'

import sqlite3
import pandas as pd

def test():
	print('\n\nTesting queries written in chinook-queries.py against chinook-queries.sql:')
	nsuccess = 0
	ntest = 10
	print(f'- Success Rate: {nsuccess}/{ntest}')		
	for i in range(1,ntest+1):
		nsuccess += test_query(f'query{i}')
		print(f'- Success Rate: {nsuccess}/{ntest}')		
	
	return

def test_query(test):
	print(f'- Testing {test} ...')
	testdf = pd.read_csv(f"./data/{test}.csv")
	df = pd.read_csv(f"./data/{test}a.csv")
	try:
		diff = testdf.compare(df)
		if not len(diff):
			print(f'... passed.\n')
			return 1
		else:
			print(f'... failed. Here are the differences.\n')
			print(diff)
			return 0
	except ValueError:
		print('ValueError: the two DataFrames don’t have identical labels or shape.\n')
		return 0
	return 0

test()
