import unittest
import os
import sys

from gedcom_file_parser import print_pretty_table
import util_date
import US07_US08_Test_Suite
import unit_test_us1_us2_us3_us4_us5_us6_us10

if __name__ == '__main__':
    
    dir_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
    # dir_path = os.getcwd("../");
    print_pretty_table(f"{dir_path}/data/project01.ged")
    suit1 = unittest.TestLoader().loadTestsFromModule(util_date)
    suit2 = unittest.TestLoader().loadTestsFromModule(unit_test_us1_us2_us3_us4_us5_us6_us10)
    suit3 = unittest.TestLoader().loadTestsFromModule(US07_US08_Test_Suite)
    result1 = unittest.TextTestRunner(verbosity=2).run(suit1).wasSuccessful()
    result2 = unittest.TextTestRunner(verbosity=2).run(suit2).wasSuccessful()
    result3 = unittest.TextTestRunner(verbosity=2).run(suit3).wasSuccessful()

    sys.exit(result1)