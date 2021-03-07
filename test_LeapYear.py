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
        def test_LeapYearDiv4(self):
                #Testing Leap years that are divisible by 4
                result = LeapYear.LeapYear(4)
                self.assertEqual(result, True)
                
                
                result = LeapYear.LeapYear(8)
                self.assertEqual(result, True)
                
                
                result = LeapYear.LeapYear(12)
                self.assertEqual(result, True)
                result = LeapYear.LeapYear(40)
                self.assertEqual(result, True)
                
                result = LeapYear.LeapYear(180)
                self.assertEqual(result, True)

                result = LeapYear.LeapYear(1004)
                self.assertEqual(result, True)       

        def test_LeapYearDiv100(self):
                #Testing Leap years that are divisible by 100 but not 400
                result = LeapYear.LeapYear(100)
                self.assertEqual(result, False)
                
                
                result = LeapYear.LeapYear(200)
                self.assertEqual(result, False)
                
                
                result = LeapYear.LeapYear(1100)
                self.assertEqual(result, False)
                 
        def test_LeapYearDiv100(self):
                #Testing Leap years that are divisible by 400
                result = LeapYear.LeapYear(400)
                self.assertEqual(result, True)
                
                
                result = LeapYear.LeapYear(800)
                self.assertEqual(result, True)
                
                
                result = LeapYear.LeapYear(1600)
                self.assertEqual(result, True)


                
if __name__ == "__main__":
        unittest.main()
