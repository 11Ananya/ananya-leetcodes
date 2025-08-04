class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        temp=str(x)
        if str(x)==temp[::-1]:
            return True
        else:
            return False