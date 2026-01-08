"""
Factorial of a number is the product of all positive integers less than or equal
to that number.
Example 1
Input: n = 2
Output: 2
Explanation: 2! = 1 * 2 = 2.

Example 2
Input: n = 0
Output: 1
Explanation: 0! is defined as 1.
"""
def factorial_number(num):
    if num==1 or num==0:
        return 1
    return factorial_number(num-1)*num

print(factorial_number(5))