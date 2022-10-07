# -*- coding: utf-8 -*-

"""
Using sqlite in Python
October 6, 2022
"""

__author__ = 'Jacob Shusko'

import sqlite3
import pandas as pd

def queries():
	# connect to local instance of chinook.db
	with sqlite3.connect("chinook.db") as con:
		cur = con.cursor()
			
		# read in queries to be written
		queries = open('doc/queries.txt','r').read().split("\n")[:-1]
		
		print(queries[0])
		res1,cmd1 = query1(cur)
		print(f"sql: {cmd1}")
		headers1 = [tuple[0] for tuple in cur.description]
		print(headers1)
		df = pd.DataFrame(data=res1,columns=headers1)
		print(df)
		df.to_csv("data/query1a.csv",index=False)
		
		print("\n"+queries[1])
		res2,cmd2 = query2(cur)
		print(f"sql: {cmd2}")
		headers2 = [tuple[0] for tuple in cur.description]
		df = pd.DataFrame(data=res2,columns=headers2)
		print(df)
		df.to_csv("data/query2a.csv",index=False)
		
		print("\n"+queries[2])
		res3,cmd3 = query3(cur)
		print(f"sql: {cmd3}")
		headers3 = [tuple[0] for tuple in cur.description]
		df = pd.DataFrame(data=res3,columns=headers3)
		print(df)
		df.to_csv("data/query3a.csv",index=False)	
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
		select c.firstname, c.lastname, i.invoiceid, i.invoicedate, i.billingcountry
		from customers as c, invoices as i
		where c.country = 'Brazil' and
		c.customerid = i.customerid;
		"""
	res = cur.execute(cmd)	
	return res,cmd

def query4(cur):
	"""
	4. Provide a query showing only the Employees who are Sales Agents. 
	"""
	cmd = """
		select c.firstname, c.lastname, i.invoiceid, i.invoicedate, i.billingcountry
		from customers as c, invoices as i
		where c.country = 'Brazil' and
		c.customerid = i.customerid;
		"""
	res = cur.execute(cmd)	
	return res,cmd

queries()		
