#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 10:32:56 2023

@author: student
"""

A = []
def introll():
    global t
    t=int(input("Enter the total number of student :"))
    for i in range(t):
        x=int(input(f"Enter the roll no of student No {i + 1}:"))
        A.append(x)
    print(" List of Student",A)


def Search_l(A):
    n=int(input("Enter Roll No of Student you Want to search using Sequential:"))
    for i in range(len(A)):
        if ( A[i]==n ):
           print("Student Attended Training Programe found at",i+1)
           break
    else:
        print("Student Not Found.")


def Search_s(A):
    n=int(input("Enter Roll No of Student you Want to search using sentinental:"))
    last= A[t-1]
    A[t-1] = n
    i=0
    while (A[i] != n):
        i=i+1
    A[t-1]=last
    if(i < t-1 or A[t-1]==n):
        print("Student Attended Training Programe Found At",i+1)
    else:
        A.append(n)
        print("Student Found at",t+1)
    print("New List:",A)
        


while True:
    print("***MENU***")
    print("1.Accept list of Students")
    print("2.Linear Search")
    print("3.Sentinental Search")
    print("4.Exit")
    c=int(input("Enter Choice"))
    if c==1:
        introll()
    elif c==2:
        Search_l(A)
    elif c==3:
        Search_s(A)
    elif c==4:
        break