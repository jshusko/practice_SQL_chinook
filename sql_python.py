# -*- coding: utf-8 -*-

"""
Using sqlite in Python
October 6, 2022
"""

__author__ = 'Jacob Shusko'

import sqlite3

def queries():
	# connect to local instance of chinook.db
	with sqlite3.connect("chinook.db") as con:
		cur = con.cursor()
		
		# read in queries to be written
		queries = open('queries.txt','r').read().split("\n")[:-1]
		
		
		print(queries[0])
		res1,cmd1 = query1(cur)
		print(f"sql: {cmd1}")
		for row in res1:
			print(row)		

		print(f"\n{queries[1]}")
		res2,cmd2 = query2(cur)
		print(f"sql: {cmd2}")
		for row in res2:
			print(row)		
		
		print(f"\n{queries[2]}")
		res3,cmd3 = query3(cur)
		print(f"sql: {cmd3}")
		for row in res3:
			print(row)		
		
		return

def query1(cur):
	"""
	1. Provide a query showing Customers (just their full names, customer ID and country) who are not in the US.
	"""
	cmd = "SELECT CustomerId, FirstName, LastName, Country FROM customers WHERE Country != 'USA'"
	res = cur.execute(cmd)	
	return res,cmd

def query2(cur):
	"""
	2. Provide a query only showing the Customers from Brazil.
	"""
	cmd = "SELECT * FROM customers WHERE Country = 'Brazil'"
	res = cur.execute(cmd)	
	return res,cmd

def query3(cur):
	"""
	3. Provide a query showing the Invoices of customers who are from Brazil. The resultant table should show the customer's full name, Invoice ID, Date of the invoice and billing country.
	"""
	cmd = """
		SELECT c.FirstName, c.LastName, i.InvoiceID, i.InvoiceDate, i.BillingCountry  
		FROM customers as c, invoices as i 
		WHERE i.InvoiceId = c.CustomerId and c.Country = 'Brazil'
		"""
	res = cur.execute(cmd)	
	return res,cmd

queries()		
