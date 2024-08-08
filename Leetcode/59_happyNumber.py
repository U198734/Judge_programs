'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def entero_a_array(numero):
            return [int(digito) for digito in str(numero)]

        def sum_power(numero):
            digits = entero_a_array(numero)
            return sum(d ** 2 for d in digits)
        
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum_power(n)
            
        return n == 1




