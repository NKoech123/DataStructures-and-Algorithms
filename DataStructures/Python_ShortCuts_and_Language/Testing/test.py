import unittest

class Test(unittest.TestCase):
    def sum(self, x,y):
        return x+y

    def test(self):
        val = self.sum(1,1)
        self.assertEqual(val, 2)

if __name__ == '__main__':
    unittest.main()