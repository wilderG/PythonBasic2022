mport os
import sys


#This is a helloword program 

def string_list(mylist:str):

    print("This is a String list")
    count = 0
# This is a for look that will iterate througth the list called mylist
    for i in mylist:
        print("Iteration number",i)
        # count +=1
        count = count + 1
    print("Loop total iterations",count)

def interger_list(mylist2:int):

    print("This is a interger list")
    count = 0
# This is a for look that will iterate througth the list called mylist
    for i in mylist2:
        print("Iteration number",i)
        # count +=1
        count = count + 1
    print("Loop total iterations",count)

if __name__ == "__main__":
    # Setting list of strings and integers
    mylist = ['0','1','2', '3','4','5','6','7','8','9']
    mylist2 =[0,1,2,3,4,5,6,7,8,9]
    # This functions takes a list of strings 
    string_list(mylist)
    # This funtion takes a list of integers
    interger_list(mylist2)%                  