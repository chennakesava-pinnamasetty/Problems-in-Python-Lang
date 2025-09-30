


# 1 Write a python program to find out common letters between two strings.

       # This coding str1 and str2 saparate saparate

# Ex : NAINA = N A I              This give kis this
def common_letters():
    str1 = input("Enter first string :")
    str2 = input("Enter second string :")

    s1 = set(str1)
    s2 = set(str2)
    print(s1)
    print(s2)       

common_letters()
                #{'N', 'A', 'I'}
                #{'E', 'A', 'N', 'R'}


# but this compare two string give common string

def common_Word():
    str1 = input("Enter first string : ")
    str2 = input("Enter second string :")

    s1 = set(str1)
    s2 = set(str2)
    total = s1 & s2

    print(total)

common_Word()

                     # Enter first string : REENA
                     # Enter second string :NAINA
                     # {'N', 'A'}




# 2 How To Swap First & Last Elements of a List

# 1
mylist = [1,2,3,4,5]
size = len(mylist)

temp = mylist[0]
mylist[0] = mylist[size -1]
mylist[size -1] = temp

print("list after swapping :",mylist)           # list after swapping : [5, 2, 3, 4, 1]


# 2. Approach

mylist = [10,20,30,40,50]
mylist[0],mylist[size -1] = mylist[size -1],mylist[0]
print("list after swapping :",mylist)                  # [50, 20, 30, 40, 10]


# 3 using tuple

mylist = [100,200,300,400,500]
get = (mylist[-1],mylist[0])
mylist[0],mylist[-1] = get
print("list after swapping :",mylist)         #  [500, 200, 300, 400, 100]


# 4 * Operand

mylist = [101,102,103,104,105]

start,*middle,end = mylist

mylist = [end,*middle,start]
print("list after swapping :",mylist)    # list after swapping : [105, 102, 103, 104, 101]

