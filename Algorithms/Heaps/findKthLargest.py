import unittest
class Solution:
    
    def findKthLargest(self,nums  , k:int ) -> int:
        import heapq
        return heapq.nlargest(k,nums)[-1]

class TestingSolution(unittest.TestCase):
    def test_funcRes(self):
        self.assertEqual(self.func_runner(),  4)

    def func_runner(self):
        kth=Solution().findKthLargest([3,2,3,1,2,4,5,5,6] , 4 ) 
        return kth

if __name__ == "__main__":
    k,nums=4, [3,2,3,1,2,4,5,5,6]
    
    kth=Solution().findKthLargest(nums , k ) 

    print(kth)
    
    unittest.main()


