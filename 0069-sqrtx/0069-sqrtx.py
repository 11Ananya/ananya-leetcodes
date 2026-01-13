class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        sqrt = 1
        while sqrt*sqrt <= x:
            sqrt+=1
        return sqrt-1

