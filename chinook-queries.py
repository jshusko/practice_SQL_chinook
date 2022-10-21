# -*- coding: utf-8 -*-

"""
Using sqlite in Python
October 6, 2022
"""

__author__ = 'Jacob Shusko'

import sqlite3
import pandas as pd
import sys

thismodule = sys.modules[__name__]
nimplemented = 10

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
		SELECT * FROM Employees WHERE Title='Sales Support Agent';
		"""
	res = cur.execute(cmd)	
	return res,cmd

def query5(cur):
	"""
	5. Provide a query showing a unique list of billing countries from the Invoice table. 
	"""
	cmd = """
		SELECT DISTINCT BillingCountry FROM Invoices
		"""
	res = cur.execute(cmd)
	return res,cmd

def query6(cur):
	"""
	6. Provide a query showing the invoices of customers who are from Brazil.
	"""
	cmd = """
		select *
		from customers as c, invoices as i
		where c.country = 'Brazil' and
		c.customerid = i.customerid;
		"""
	res = cur.execute(cmd)
	return res,cmd

def query7(cur):
	"""
	7. Provide a query that shows the invoices associated with each sales agent. 
	The resultant table should include the Sales Agent's full name.
	"""
	cmd = """
		select e.firstname, e.lastname, InvoiceId, i.CustomerId, i.InvoiceDate, i.BillingAddress, i.BillingCountry, i.BillingPostalCode, i.Total 
		from invoices as i, customers as c
		left join employees as e
		where i.customerid = c.customerid and
		c.supportrepid = e.employeeid;
		"""
	res = cur.execute(cmd)
	return res,cmd

def query8(cur):
	"""
	8. Provide a query that shows the Invoice Total, Customer name, Country and Sale Agent name for all invoices and customers.	
	"""
	cmd = """
		select e.firstname as 'employee first', e.lastname as 'employee last', c.firstname as 'customer first', c.lastname as 'customer last', c.country, i.total
		from employees as e
			join customers as c on e.employeeid = c.supportrepid
			join invoices as i on c.customerid = i.customerid
		"""
	res = cur.execute(cmd)
	return res,cmd

def query9(cur):
	"""
	9. How many Invoices were there in 2009 and 2011? What are the respective total sales for each of those years?
	"""
	cmd = """
		select count(i.invoiceid), sum(i.total)
		from invoices as i
		where i.invoicedate between datetime("2009-01-01 00:00:00") and datetime("2011-12-31 00:00:00");
		"""
	res = cur.execute(cmd)
	return res,cmd

def query10(cur):
	"""
	10. Looking at the invoice_items table, provide a query that COUNTs the number of line items for Invoice ID 37.
	"""
	cmd = """
		select count(i.invoicelineid)
		from invoice_items as i
		where i.invoiceid = 37;
		"""
	res = cur.execute(cmd)
	return res,cmd

def run_queries():
	# connect to local instance of chinook.db
	with sqlite3.connect("chinook.db") as con:
		cur = con.cursor()
			
		# read in queries to be written
		queries = open('doc/queries.txt','r').read().split("\n")[:-1]
		
		print(f'\nRunning sql queries up to query {nimplemented}...\n')		
		for idx, query in enumerate(queries):		
			if idx < nimplemented:
				print(query)
				f = getattr(thismodule,f"query{idx+1}")
				res,cmd = f(cur)
				print(f"sql: {cmd}")
				headers = [tuple[0] for tuple in cur.description]
				df = pd.DataFrame(data=res,columns=headers)
				df.to_csv(f"data/query{idx+1}a.csv",index=False)
		
		return

run_queries()		
