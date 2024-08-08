class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def processString(string):
            stack = []
            for char in string:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return stack
        
        return processString(s) == processString(t)


solution = Solution()
print(solution.backspaceCompare("ab#c", "ad#c"))  
print(solution.backspaceCompare("ab##", "c#d#")) 
print(solution.backspaceCompare("a#c", "b"))      
