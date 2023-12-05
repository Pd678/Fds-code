#'''Write a simple Python program to store marks scored in subject “Fundamental of Data 
#Structure” by N students in the 
#class. Write functions to compute following: 
#a) The average score of class 
#b) Highest score and lowest score of class 
#c) Count of students who were absent for the test 
#d) Display mark with highest frequency''' 

A = []
B = []

def marksinput(A, B):
    global n
    n = int(input("Enter Number of students in class:"))
    for i in range(n):
        x = input(f"Enter the marks of student {i + 1} in FDS subject:")
        if x == 'AB' or x == 'ab':
            x = -1
            B.append(x)
        else:
            x = int(x)
            if x < 0 or x > 30:
                print("Enter valid data!!!")
                x = input(f"Enter the marks of student {i + 1} again!:")
                if x == 'AB' or x == 'ab':
                    x = -1
                    B.append(x)
                else:
                    x = int(x)
                    if x < 0 or x > 30:
                        print("Enter valid data!!!")
                    A.append(x)
            else:
                A.append(x)

def average(A):
    if len(A) > 0:
        avg = sum(A) / len(A)
    else:
        avg = 0
    print("Average Score of the class:", avg)

def highest(A):
    global highest
    highest = max(A)
    print("Highest Score in the class:", highest)

def lowest(A):
    lowest = min(A)
    print("Lowest Score in the class: ", lowest)

def absent(B):
    print("Number of absent Students:", B.count(-1))

def freq(A):
    print("Display mark with the highest frequency: ", highest, "Count", A.count(highest))

def main():
    print("MENU")
    print("1. List of Marks")
    print("2. Average Marks")
    print("3. Highest Marks")
    print("4. Lowest Marks")
    print("5. Absent Marks")
    print("6. Highest Frequency")

    c = int(input("Enter Your Choice to Continue: "))

    if c == 1:
        print("Marks list:", A)
    elif c == 2:
        average(A)
    elif c == 3:
        highest(A)
    elif c == 4:
        lowest(A)
    elif c == 5:
        absent(B)
    elif c == 6:
        freq(A)
    else:
        print('Enter Valid Choice!')

if __name__ == "__main__":
    marksinput(A, B)
    main()
