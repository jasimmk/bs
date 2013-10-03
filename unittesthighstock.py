#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import random
import sys
import unittest
from datetime import datetime
from dateutil.relativedelta import relativedelta

from highstock import Stock, StockException

class TestStock(unittest.TestCase):
    """
    Unittests for the Stock Class
    """

    def setUp(self):
        self.fp = 'data-valid1.csv'
        self.invalidfp = 'data-invalid.csv'
        self.no_companies = 10
        self.generate_csv()
        self.generate_invalid_csv()

    def tearDown(self):
        try:
            #os.remove('data-valid1.csv')
            #os.remove('data-invalid.csv')
            pass
        except:
            pass
    def month_iterator(self, from_date = "01/01/1990", to_date = "01/10/2013"):
        """

        """
        current_month = datetime.strptime(from_date,"%d/%m/%Y")
        to_month = datetime.strptime(to_date,"%d/%m/%Y")   

        while current_month <= to_month:
            yield current_month
            current_month = current_month + relativedelta(months = +1 )

        return

    def generate_csv(self):

        with open(self.fp,'wb') as csvfile:
            
            datawriter = csv.writer(csvfile, delimiter =',', quotechar='"')
            header = list(["year","month"])
            for icompany in xrange(self.no_companies):
                header.append('Company_%s'%icompany) 
                
            datawriter.writerow(header)

            for i in self.month_iterator('01/01/1990','01/10/2013'):
                row = [i.strftime("%Y"),i.strftime("%b")]
                for icomp in xrange(self.no_companies):
                    row.append(random.randint(10,50)*(icomp + 1))
                #print row
                datawriter.writerow(row)

    def generate_invalid_csv(self):
        with open(self.invalidfp,'wb') as csvfile:
            
            datawriter = csv.writer(csvfile, delimiter =',', quotechar='"')
            header = list(["year","month"])
            for icompany in xrange(self.no_companies):
                header.append('Company_%s'%icompany) 
                
            datawriter.writerow(header)

            for i in self.month_iterator('01/01/1990','01/10/2013'):
                row = [i.strftime("%Y"),i.strftime("%b")]
                for icomp in xrange(self.no_companies):
                    row.append(random.randint(10,50)*(icomp + 1))
                #print row
                row.append("invalid Data");
                datawriter.writerow(row)        

    def test_success(self):
        """
        Test the Workin of Module
        checks __init__, find_highest, check_format and print_highest
        """      
        x = Stock(self.fp)    
        self.assertTrue(x.print_highest())

    def test_invalid_csvdata(self):
        x = Stock(self.invalidfp)  
        self.assertRaises(StockException, x.print_highest)        

    def test_invalid_filename(self):
        """
        Exception Raises if Invalid file name or Invalid formatted CSV Given
        """

        self.assertRaises(StockException, Stock, 'invalid_file.csv')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStock)
    unittest.TextTestRunner(verbosity=2).run(suite)            
    sys.exit() 