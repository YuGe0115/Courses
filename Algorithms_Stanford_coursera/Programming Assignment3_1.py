# Requirement: For the first part of the programming assignment, you should always use the first element of the array as the pivot element.

def partition(arr,left,right):
    n = len(left)
    pivot = arr[n]
    i,j = len(left)-1,len(left)