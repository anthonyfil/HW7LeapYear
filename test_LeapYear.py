import unittest
import LeapYear
class test_LeapYear(unittest.TestCase): 
        def test_LeapYearNotLeap(self):
                #Testing Numbers
                result = LeapYear.LeapYear(1)
                self.assertEqual(result, False)
                
                
                result = LeapYear.LeapYear(2)
                self.assertEqual(result, False)
                
                
                result = LeapYear.LeapYear(3)
                self.assertEqual(result, False)
                result = LeapYear.LeapYear(75)
                self.assertEqual(result, False)
                
                result = LeapYear.LeapYear(901)
                self.assertEqual(result, False)

                result = LeapYear.LeapYear(279)
                self.assertEqual(result, False)
        
                
if __name__ == "__main__":
        unittest.main()
