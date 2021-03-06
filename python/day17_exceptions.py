#!/usr/bin/python3
#
# Exceptions
# https://www.hackerrank.com/contests/30-days-of-code/challenges/day-17-exceptions

class Calculator:
    def power(self, n, p):
        if (n < 0 or p <0):
            raise Exception("n and p should be non-negative")
        else:
            return n**p

myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n,p)
        print("ans=", ans)
    except Exception as e:
        print("e=", e)


"""
input:
4
3 5
2 4
-1 -2
-1 3

output:
243
16
n and p should be non-negative
n and p should be non-negative


problem:
Create a class Calculator which consists of a single method power(int,int). This method takes two integers, n and p, as parameters and finds n^p. If either n or p is negative, then the method must throw an exception which says "n and p should be non-negative". 

Note: The class Calculator mustn't be public.

First line contains T, the number of test cases. Next T lines contain two integers n and p separated by a space.

"""
