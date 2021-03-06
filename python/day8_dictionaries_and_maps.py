#!/usr/bin/python3
#
# Dictionaries and Maps
# 
# https://www.hackerrank.com/contests/30-days-of-code/challenges/day-8-dictionaries-and-maps

N=int(input().strip())

phonebook = {}
for i in range(N):
    name = input().strip()
    phone = input().strip()
    phonebook[name] = phone
    
name = input().strip()
while name != '':

    if name in phonebook:
        print(name + "=" + phonebook[name])
    else:
        print("Not found")

    name = input().strip()


"""
problem:
The first line will have an integer N denoting the number of entries in the phone book. Each entry consists of two lines: a name and the corresponding phone number.

After these, there will be some queries. Each query will contain name of a friend. Read the queries until end-of-file.

input:
3
sam
99912222
tom
11122222
harry
12299933
sam
edward
harry

output:
sam=99912222
Not found
harry=12299933
"""
