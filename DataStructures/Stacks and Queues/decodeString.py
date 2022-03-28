'''
s= "3[a2[c]]"
           ^
stack =   3[a  c c  
stack =[ a c c  a c c] #each elem is a str
->  'accacc'
decode ->  acc acc acc


'''
import unittest

class Solution:
    def decodeString(self, s):

        stack=[]

        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                substr=''
                while stack[-1] !='[':
                    substr = stack.pop() + substr
                stack.pop()
                k=''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                substr = int(k) * substr
                stack.append(substr)

        return "".join(stack)
                


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

   
