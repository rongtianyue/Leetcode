class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        Map = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c not in Map:
                stack.append(c)
            if c in Map:
                if not stack or stack[-1] != Map[c]:
                    return False
                stack.pop()

        return not stack
        '''
        arr = []

        for i in range(len(s)):
            if s[i] == '(':
                arr.append(s[i])
            if s[i] == '{':
                arr.append(s[i])
            if s[i] == '[':
                arr.append(s[i])
            if s[i] == ')':
                if not arr or (arr.pop() != '('):
                    return False
            if s[i] == '}':
                if not arr or (arr.pop() != '{'):
                    return False
            if s[i] == ']':
                if not arr or (arr.pop() != '['):
                    return False

        if arr:
            return False
        return True'''