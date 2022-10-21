.headers on
.mode csv
.echo off
-- 1. Provide a query showing Customers (just their full names, customer ID and country) who are not in the US.
.output data/query1.csv
select customerid, firstname, lastname, country
from customers
where not country = 'USA';
.output stdout

-- 2. Provide a query only showing the Customers from Brazil.
.output data/query2.csv
select * from customers
where country = 'Brazil';
.output stdout

-- 3. Provide a query showing the Invoices of customers who are from Brazil. The resultant table should show the customer's full name, Invoice ID, Date of the invoice and billing country.
.output data/query3.csv
select c.firstname, c.lastname, i.invoiceid, i.invoicedate, i.billingcountry
from customers as c, invoices as i
where c.country = 'Brazil' and
c.customerid = i.customerid;
.output stdout

-- 4. Provide a query showing only the Employees who are Sales Agents.
.output data/query4.csv
select * from employees
where employees.title = 'Sales Support Agent';
.output stdout

-- 5. Provide a query showing a unique list of billing countries from the Invoice table.
.output data/query5.csv
select distinct billingcountry from invoices;
.output stdout

-- 6. Provide a query showing the invoices of customers who are from Brazil.
.output data/query6.csv
select *
from customers as c, invoices as i
where c.country = 'Brazil' and
c.customerid = i.customerid;
.output stdout

-- 7. Provide a query that shows the invoices associated with each sales agent. The resultant table should include the Sales Agent's full name.
.output data/query7.csv
select e.firstname, e.lastname, i.invoiceid, i.customerid, i.invoicedate, i.billingaddress, i.billingcountry, i.billingpostalcode, i.total
from customers as c, invoices as i
on c.customerid = i.customerid
join employees as e
on e.employeeid = c.supportrepid
order by e.employeeid;
.output stdout

-- 8. Provide a query that shows the Invoice Total, Customer name, Country and Sale Agent name for all invoices and customers.
.output data/query8.csv
select e.firstname as 'employee first', e.lastname as 'employee last', c.firstname as 'customer first', c.lastname as 'customer last', c.country, i.total
from employees as e
	join customers as c on e.employeeid = c.supportrepid
	join invoices as i on c.customerid = i.customerid;
.output stdout

-- 9. How many Invoices were there in 2009 and 2011? What are the respective total sales for each of those years?
.output data/query9.csv
select count(i.invoiceid), sum(i.total)
from invoices as i
where i.invoicedate between datetime('2011-01-01 00:00:00') and datetime('2011-12-31 00:00:00');
.output stdout

-- 10. Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for Invoice ID 37.
.output data/query10.csv
select count(i.invoicelineid)
from invoice_items as i
where i.invoiceid = 37;
.output stdout

-- 11. Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for each Invoice. HINT: [GROUP BY](http://www.sqlite.org/lang_select.html#resultset)
.output data/query11.csv
select invoiceid, count(invoicelineid)
from invoiceline
group by invoiceid;
.output stdout

-- 12. Provide a query that includes the track name with each invoice line item.
.output data/query12.csv
select i.*, t.name
from invoiceline as i, track as t
on i.trackid = t.trackid;
.output stdout

-- 13. Provide a query that includes the purchased track name AND artist name with each invoice line item.
.output data/query13.csv
select i.*, t.name as 'track', ar.name as 'artist'
from invoiceline as i
	join track as t on i.trackid = t.trackid
	join album as al on al.albumid = t.albumid
	join artist as ar on ar.artistid = al.artistid;
.output data/query13.csv

-- 14. Provide a query that shows the # of invoices per country. HINT: [GROUP BY](http://www.sqlite.org/lang_select.html#resultset)
.output data/query14.csv
select billingcountry, count(billingcountry) as '# of invoices'
from invoice
group by billingcountry;
.output stdout

-- 15. Provide a query that shows the total number of tracks in each playlist. The Playlist name should be include on the resultant table.
.output data/query15.csv
select *, count(trackid) as '# of tracks'
from playlisttrack, playlist
on playlisttrack.playlistid = playlist.playlistid
group by playlist.playlistid;
.output stdout

-- 16. Provide a query that shows all the Tracks, but displays no IDs. The resultant table should include the Album name, Media type and Genre.
.output data/query16.csv
select t.name as 'track', t.composer, t.milliseconds, t.bytes, t.unitprice, a.title as 'album', g.name as 'genre', m.name as 'media type'
from track as t
	join album as a on a.albumid = t.albumid
	join genre as g on g.genreid = t.genreid
	join mediatype as m on m.mediatypeid = t.mediatypeid;
.output stdout

-- 17. Provide a query that shows all Invoices but includes the # of invoice line items.
.output data/query17.csv
select invoices.*, count(invoiceline.invoicelineid) as '# of line items'
from invoices, invoiceline
on invoice.invoiceid = invoiceline.invoiceid
group by invoice.invoiceid;
.output stdout

-- 18. Provide a query that shows total sales made by each sales agent.
.output data/query18.csv
select e.*, count(i.invoiceid) as 'Total Number of Sales'
from employees as e
	join customers as c on e.employeeid = c.supportrepid
	join invoices as i on i.customerid = c.customerid
group by e.employeeid;
.output stdout

-- 19. Which sales agent made the most in sales in 2009?
.output data/query19.csv
select *, max(total) from
(select e.*, sum(total) as 'Total'
from employees as e
	join customers as c on e.employeeid = c.supportrepid
	join invoices as i on i.customerid = c.customerid
where i.invoicedate between '2009-01-00' and '2009-12-31'
group by e.employeeid);
.output stdout


-- 20. Which sales agent made the most in sales in 2010?
select *, max(total) from
(select e.*, sum(total) as 'Total'
from employees as e
	join customers as c on e.employeeid = c.supportrepid
	join invoices as i on i.customerid = c.customerid
where i.invoicedate between '2010-01-00' and '2010-12-31'
group by e.employeeid)

-- 21. Which sales agent made the most in sales over all?
select *, max(total) from
(select e.*, sum(total) as 'Total'
from employees as e
	join customers as c on e.employeeid = c.supportrepid
	join invoices as i on i.customerid = c.customerid
group by e.employeeid)

-- 22. Provide a query that shows the # of customers assigned to each sales agent.
select e.*, count(c.customerid) as 'TotalCustomers'
from employees as e
	join customers as c on e.employeeid = c.supportrepid
group by e.employeeid

-- 23. Provide a query that shows the total sales per country. Which country's customers spent the most?
select i.billingcountry, sum(total) as 'TotalSales'
from invoice as i
group by billingcountry
order by totalsales desc

-- 24. Provide a query that shows the most purchased track of 2013.
select *, count(t.trackid) as count
from invoiceline as il
	join invoices as i on i.invoiceid = il.invoiceid
	join track as t on t.trackid = il.trackid
where i.invoicedate between '2013-01-01' and '2013-12-31'
group by t.trackid
order by count desc

-- 25. Provide a query that shows the top 5 most purchased tracks over all.


-- 26. Provide a query that shows the top 3 best selling artists.


-- 27. Provide a query that shows the most purchased Media Type.



















