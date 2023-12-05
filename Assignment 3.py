A = []

def matinp1():  
    global m, n
    m = int(input("Enter number of Rows in matrix 1: "))
    n = int(input("Enter number of Columns in matrix 1: "))
    print("***Example***")
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            print(f'A{i}{j}', end=' ')
        print()
    for i in range(m):
        for j in range(n):
            e = int(input(f"Enter Element A{i + 1}{j + 1} of Matrix 1: "))
            A.append(e)

matinp1()
print("\nMatrix 1:")

def display(matrix, rows, columns):
    for i in range(rows):
        for j in range(columns):
            print(matrix[i * columns + j], end=' ')
        print()

display(A, m, n)

B = []

def matinp2():
    global x, y
    x = int(input("Enter number of Rows in matrix 2: "))
    y = int(input("Enter number of Columns in matrix 2: "))
    print("***Example***")
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            print(f'B{i}{j}', end=' ')
        print()
    for i in range(x):
        for j in range(y):
            e = int(input(f"Enter Element B{i + 1}{j + 1} of Matrix 2: "))
            B.append(e)

matinp2()
print("\nMatrix 2:")

add = []
sub = []
mul = []
trans = []

def add_mat():
    global add
    if (m != x or n != y):
        print("Addition cannot be performed. Enter valid matrices!")
    else:
        add = []
        for i in range(0, len(A)):
            add.append(A[i] + B[i])
        print("\nAddition is:")
        display(add, x, n)

def sub_mat():
    global sub
    if (m != x or n != y):
        print("Subtraction cannot be performed. Enter valid matrices!")
    else:
        sub = []
        for i in range(0, len(A)):
            sub.append(A[i] - B[i])
        print("\nSubtraction is:")
        display(sub, m, y)

def trans_mat():
    global trans
    trans = []
    for i in range(n):
        for j in range(m):
            trans.append(A[j * n + i])
    print("\nTranspose of Matrix A:")
    display(trans, n, m)

def mul_mat():
    global mul
    if n != x:
        print("Matrix multiplication is not possible!!!")
    else:
        mul = []
        for i in range(m):
            row = []
            for j in range(y):
                total = 0
                for k in range(n):
                    total += A[i * n + k] * B[k * y + j]
                row.append(total)
            mul.extend(row)
        print("\nMatrix Multiplication is:")
        display(mul, m, y)

while True:
    print("\nMenu:")
    print("1. Perform Matrix Addition")
    print("2. Perform Matrix Subtraction")
    print("3. Transpose Matrix A")
    print("4. Perform Matrix Multiplication")
    print("5. Quit")
    choice = input("Enter your choice (1/2/3/4/5): ")
    if choice == "1":
        add_mat()
    elif choice == "2":
        sub_mat()
    elif choice == "3":
        trans_mat()
    elif choice == "4":
        mul_mat()
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5).")
