from US07_US08_Source_File import check_150_years_age, check_birth_before_marriage_of_parents
from util_date import Date
from gedcom_file_parser import gedcom_file_parser, print_pretty_table
import sys
import unittest
import datetime

class TestUserStories(unittest.TestCase):
   
    def test_user_stories(self):
        directory_path = '/Users/saranshahlawat/Desktop/Stevens/Semesters/Summer 2019/SSW-555/project/GEDCOM/project3/data/US07_US08_test_file.ged'
        individuals, families = gedcom_file_parser(directory_path)
        print_pretty_table(directory_path)

        #US07 Test
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        check_150_years_age(individuals)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), 'ERROR: INDIVIDUAL: US07: @I3@: More than 150 years old - Birth date 19 May 0268\nERROR: INDIVIDUAL: US07: @I9@: More than 150 years old at death - Birth date 17 Nov 0301: Death date 15 Nov 0560\n')
       
        #US08 Test
        capturedOutput2 = io.StringIO()
        sys.stdout = capturedOutput2
        check_birth_before_marriage_of_parents(families, individuals)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput2.getvalue(), 'ANOMOLY: FAMILY: US08: @F3@: Child @I7@ born 05 Sep 0287 before marriage on 16 Jun 0280\nANOMOLY: FAMILY: US08: @F3@: Child @I7@ born 05 Sep 0287 after divorce on 18 Nov 0285\n')

if __name__ == '__main__':
    unittest.main(exit=False)