#!/usr/bin/env python
# coding: utf-8

# In[95]:


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        s = s.strip() 
        if not s:
            return 0

        b = ""
        for i, char in enumerate(s):
            if i == 0 and (char == "-" or char == "+"):
                b += char
            elif char.isdigit():
                b += char
            else:
                break

        if not b or b == "-" or b == "+":
            return 0

        result = int(b)
        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX
        else:
            return result


# In[100]:


s = "-ln1 ia  number"
solution = Solution()
result = solution.myAtoi(s)
print(result)


# In[ ]:




