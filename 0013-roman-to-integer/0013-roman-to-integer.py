class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sint= 0 
        for i in range(-1, -len(s)-1, -1):
            if  i == -len(s):
                if s[i] == 'I':
                    sint+=1
                elif s[i] == 'V':
                    sint += 5
                
                elif s[i] == 'X':
                    sint += 10

                elif s[i] == 'L':
                    sint += 50
                
                elif s[i] == 'C':
                    sint += 100
                
                elif s[i] == 'D':
                    sint +=500
                
                else:
                    sint +=1000

            
            elif s[i] == 'I':
                sint+=1
            elif s[i] == 'V':
                sint += 5
                if s[i-1] and s[i-1] == 'I':
                    sint-=2

            elif s[i] == 'X':
                sint += 10
                if s[i-1] and s[i-1] == 'I':
                    sint-=2

            elif s[i] == 'L':
                sint += 50
                if s[i-1] and s[i-1] == 'X':
                    sint-=20
            elif s[i] == 'C':
                sint += 100
                if s[i-1] and s[i-1] == 'X':
                    sint-=20
            elif s[i] == 'D':
                sint +=500
                if s[i-1] and s[i-1] == 'C':
                    sint-=200
            else:
                sint +=1000
                if s[i-1] and s[i-1] == 'C':
                    sint-=200

        return sint

