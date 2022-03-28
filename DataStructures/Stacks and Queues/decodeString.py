'''
s= "3[a2[c]]"
decode ->  acc acc acc


'''
import unittest

class Solution:
    def decodeString(self, s):
        
        return "accaccacc"

class TestClass(unittest.TestCase):
    
    def testfunc(self):
        test_sol = Solution()
        res=test_sol.decodeString("3[a2[c]]")
        expected="accaccacc"

        self.assertEqual(res, expected)




if __name__ == "__main__":
    sol=Solution()

    #return and print solution
    sol.decodeString("3[a2[c]]")
    print(sol.decodeString("3[a2[c]]"))

    #run unittest
    unittest.main()

   
