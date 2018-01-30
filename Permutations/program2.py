from functools import reduce

#global variable to count recursions
global_count = 0

def persistence(a):
    if len(str(a))<=1 :
        #defining the counter as global variable
        global global_count
        #return recursion count
        return global_count
    else:
        #global global_count
        #increasing the count for every recursion
        global_count += 1
        result =1
        #result=reduce(lambda x,y:x*y,[int(i) for i in str(a)])  #function that does the same as the for loop (not sure if we were alowed to use it
        for i in range (len(str(a))):
           result *= int (str(a)[i])
        #end of recursion whenever we have one digit number
        if result<10 and result>=0:
            return result
        #calling recursion if we we have at least a two digit number
        else:
            persistence(result)
            #return recursion count
            return global_count

#checking for input
try:
    numb = int(input("enter the number: "))
    # calling method
    print(str(persistence(numb)))
except ValueError:
        print("Sorry, wrong input!")
