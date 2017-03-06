#!/bin/python3

if __name__ == '__main__':
    n = int(input())
if n %2 !=0:
    print ('Weird')
if n %2 == 0:
    if n in range (2,5) or n > 20:
        print ('Not Weird')
    if n in range (6,20):
        print ('Weird')