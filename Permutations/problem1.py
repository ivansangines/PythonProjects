#visited = {}
#list to store the letters of the word
import pprint
combinations = []

def permute(word,i):
    #condition to finish the recursion call
    if i>=len(word):
        #visited[''.join(word)]=''
        #initialize a string where we are going to store each word combination
        temp_word =""
        #for loop to store each combination
        for i in range(len(word)):
            #creating each combination
            temp_word += word[i]
        #checking if the word is already in the list
        if temp_word not in combinations:
            #adding new combination
            combinations.append(temp_word)
        return
    #for loop for swaping, swap is going to occur with recursion calls
    for x in range(i,len(word)):
        #swaping letters (on the first trial there is no swap)
        word[x],word[i] = word [i],word[x]
        #word [i] = word [x]
        #recursion call
        permute(word,i+1)
        #swap back after recursion
        word[x],word[i] = word [i],word[x]
#        word [x] = word [i]
 #       word [i] = word [x]

permute(list("hello"),0)
#for key in visited:
    #combinations.append(key)
for item in combinations:
    print(item )

