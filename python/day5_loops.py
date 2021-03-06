#!/usr/bin/python3
#
# https://www.hackerrank.com/contests/30-days-of-code/challenges/day-5-loops

import sys

n = int(input().strip())
for i in range(n):
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

    a = arr[0] 
    b = arr[1]
    N = arr[2]
    sum = a
   
    string = ''
    for index in range(N):
        sum +=  2**index * b
        string = string + str(sum) + ' '
        
    print(string)

"""
Given three integers a, b, and N, output the following series:

a + (2^0 * b), a + (2^0 * b) + (2^1 * b), ..., a + (2^0 * b) + (2^1 * b) + ... + (2^N−1 * b)

input:
2    
5 3 5
0 2 10

output:
8 14 26 50 98
2 6 14 30 62 126 254 510 1022 2046

In the first case: a=5, b=3 ,N=5
1st term =  5+(20×3)=8
2nd term =  5+(20×3)+(21×3)=14
3rd term =  5+(20×3)+(21×3)+(22×3)=26
4th term =  5+(20×3)+(21×3)+(22×3)+(23×3)=50
5th term =  5+(20×3)+(21×3)+(22×3)+(23×3)+(24×3)=98

"""
