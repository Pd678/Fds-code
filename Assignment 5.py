A=[]
B=[]
def arr_inp():
    n=int(input("Enter number of element in an array:"))
    for i in range(n):
        x=float(input(f"Enter the Element {i + 1} of an array:"))
        A.append(x)
        B.append(x)
arr_inp()
print("Unsorted array",A)

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
selection_sort(A)
print("Sorted array By Selection Sort is:", A)

def bubble_sort():
    n = len(B)
    swapped = False
    while swapped:
        swapped = False
        x = 0
        y = 1
        while y < n:
            if B[x] > B[y]:
                temp = B[x]
                B[y] = B[y]
                B[x] = temp
                swapped = True
            x += 1
            y += 1

bubble_sort()
print("Sorted Array By Bubble Sort is :",B)