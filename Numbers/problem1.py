try:
    word_list = []
    word_count=[]
    with open("File_to_be_read","r") as file:
        #spliting each word by space
        for word in file.read().split():
            temp = word
            #deleting . , ! and any signt that is not a letter
            if word[len(word)-1]=="." or word[len(word)-1]=="," or word[len(word)-1]=="!"\
                    or word[len(word)-1]=="?" or word[len(word)-1]==":" or word[len(word)-1]==";":
                word = word[:-1]
           #storing words in the list and 1 in the count list
            if word not in word_list:
                #word_list.append(word.lower())
                word_list.append(word)
                word_count.append(1)
            #increasing the count of words
            else:
                #word_count[word_list.index(word.lower())]+=1
                word_count[word_list.index(word)] += 1
    file.close()


    with open("output1.txt","w") as outputfile:
        #going through all the list
        for index in range(len(word_list)):
            #creating the string to write in the file
            word =str(word_list[index])+":"+str(word_count[index])
            outputfile.write(word)
            outputfile.write("\n")
    outputfile.close()

except ValueError:
    print("Sorry could not find the file")


try:
    word_arr = []
    with open("File_to_be_read", "r") as file:
        #spliting words by space
        for word in file.read().split():
            #deleting signs that are not letters
            if word[len(word) - 1] == "." or word[len(word) - 1] == "," or word[len(word) - 1] == "!" \
                    or word[len(word) - 1] == "?" or word[len(word) - 1] == ":" or word[len(word) - 1] == ";":
                word = word[:-1]
            #adding not repeated words into the list
            if word not in word_arr:
                word_arr.append(word)
            #case where the word is already in the list
            else:
                continue
    file.close()


    with open("output2.txt", "w") as outputfile:
        #going through the list
        for key in word_arr:
            #creating the string to write it
            word = str(key) + "," + str(len(key))
            outputfile.write(word)
            outputfile.write("\n")
    outputfile.close()




except ValueError:
    print("Sorry could not find the file")