Code Test
=========

Question
--------
```
Q)  Consider Share prices for a N number of companies given for each month since year 1990 in a CSV file.  Format of the file is as below with first line as header.
 
Year,Month,Company A, Company B,Company C, .............Company N
1990, Jan, 10, 15, 20, , ..........,50
1990, Feb, 10, 15, 20, , ..........,50
.
.
.
.
2013, Sep, 50, 10, 15............500
 
a) List for each Company year and month in which the share price was highest.
b) Submit a unit test with sample data to support your solution.   
```
Answer
-------
Program
```
Usage: highstock.py -f <csvfile>
 highstock.py -t for test
```
####Examples
```
$ python highstock.py -f data-valid.csv

$ python highstock.py -f data-invalid.csv
# For unit testing
$ python highstock.py -t 
```
####Test with Pandas
Make sure you have installed [Pandas] Data Analysis Library.
```
$python pandas-highstock.py 
```
----------------------
*jasimmk@gmail.com*

[Pandas]: http://pandas.pydata.org/
