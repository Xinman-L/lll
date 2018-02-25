
# coding: utf-8

# # Example 1

# In[10]:


"""
Write a function 'what_sign' which returns 'Positive' 'Zero' or 'Negative' when given a number
"""


def what_sign(n):
    # Your code goes here
    if n > 0:
        return 'Positive'
    elif n < 0:
        return 'Negative'
    else:
        return 'Zero'




# In[11]:


def test_what_sign():
    assert what_sign(3) == 'Positive'
    assert what_sign(0) == 'Zero'
    assert what_sign(-3) == 'Negative'


# In[12]:


test_what_sign()


# # example 2
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method
# In[16]:


#solution


# In[15]:



l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(l))


# # Q1
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
# In[19]:


def factorial(n):
    #your code here
    pass


# In[20]:


#test your results
assert factorial(8) == 40320


# # Q2
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.
# Example:
# 
# Input:
# [4,3,2,7,8,2,3,1]
# 
# Output:
# [5,6]

# In[21]:


def findDisappearedNumbers(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #your code
        return


# # Q3
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# In[22]:


def twoSum(nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
    """
    return


# # Q3
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man a plan a canal Panama" is a palindrome.
"race a car" is not a palindrome.
# In[24]:


def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """

