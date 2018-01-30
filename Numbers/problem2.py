import copy
try:#doing try catch in case the user does not put a int as an input
    rows = int(input("enter number of rows: "))
    columns = int(input("enter number of columns: "))
    #list to storw the diferent days
    box = []
    #outer for loop for the different days
    for i in range(rows):
        column=[]
        if i==0:
            #inner for loop for the diferent columns/number of mailboxes
            for j in range(columns):
                #creating the fist empty list
                column.append("c")
        else:
            #copying as deep copy(dif memory loc.) the day before
            column= copy.deepcopy(box[i-1])
            #for item in column:
            column = [item.lower() for item in column] #changing all items in the list to lowercase
            a=i+1#range in which we opening the mailboxes (every 2 second day, every 3 third day....)
            for b in range(i,columns,a):#for loop to jump throught all the mailboxes and open colsed ones and close opened ones
            #if box[i-1][b]=="c":
                if column[b]=="c":
                    column[b]="O"
            #elif box[i-1][b]=="o":
                elif column[b]=="o":
                    column[b]="C"


        box.append(column) #append every day to the list
    #for i in range(len(box)): #for loop to print the list
        #print(str(box[i]))
    for row in box:
        print (" ".join(map(str, row)))
except ValueError:
        print("Sorry, wrong input!")
