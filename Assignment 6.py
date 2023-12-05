#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 10:02:21 2023

@author: Om Borekar
"""
A=[]
B=[]
def arr_inp():
    n=int(input("Enter number of Student in First Engineering Department:"))
    for i in range(n):
        x=float(input(f"Enter the Marks of Roll no: {i + 1} of Department:"))
        A.append(x)
        B.append(x)
arr_inp()
print("Unsorted array",A)

def partition(array, low, high):
	pivot = array[high]
	i = low - 1
	
	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			(array[i], array[j]) = (array[j], array[i])
	(array[i + 1], array[high]) = (array[high], array[i + 1])
	return i + 1
def quickSort(array, low, high):
	if low < high:

		pi = partition(array, low, high)

		quickSort(array, low, pi - 1)

		quickSort(array, pi + 1, high)
print("Unsorted Array")
print(A)
 
size = len(A)
 
quickSort(A, 0, size - 1)
 
print('Sorted Array in Ascending Order:')
print(A)

def display():
    print("***Top 5 Student of Class***")
    for i in range(0,5):
        print("Roll no:",(B.index(A[4-i]))+1,"Marks Percentage:",A[4-i])
display()
