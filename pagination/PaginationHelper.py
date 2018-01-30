# TODO: complete this class
import copy
class PaginationHelper:
    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection = None, items_per_page = 0):
        if collection is None:
            self.collection = []
            self.items_number = items_per_page
        else:#whenever we have a none empty list
            self.counter = 0 #counter to know how many elements we will add
            #creating a list with list element. Each list will have the number of elements that we are supposed to have in each page
            self.collection = [collection[i:i + items_per_page]for i in range(0, len(collection), items_per_page)]
            self.items_number = items_per_page

	# returns the number of items within the entire collection
    def item_count(self):

        for i in range(len(self.collection)):#going thought each element of the main list
            for j in range(len(self.collection[i])):#going thourgh each element of the sublists
                self.counter+=1 #increment counter every time
        print(self.counter)


	
	# returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        # it = [iter(self.collection)]*self.items_number
        # list_pages = list (zip(*it))
        # if page > (len(list_pages)-1):
        # print(-1)
        # else:
        # print(len(list_pages[page])) Does not work when len is not divisible by n

        # list_pages = [self.collection[i:i + page]for i in range(0, len(self.collection), page)]
        if page_index > (len(self.collection)) or page_index<0: #return -1 for index out of range
            print(-1)
        else:#whenever the index is in the correct range
            print(len(self.collection[page_index]))

    # returns the number of pages
    def page_count(self):
        print(len(self.collection))
		
	
	# determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index >= self.counter or item_index<0:
            print(-1)
        else:
            #page_number = (i for i, v in enumerate(self.collection) if v==item_index)
            page_number = item_index//(len(self.collection)-1) #finding the page number in a zero based index
            print(str(page_number))

try:
    data_list = []
    file = input("Enter file name: ")
    with open(file,"r") as file:
        for word in file.read().split(','):
            data_list.append(word)

    helper = PaginationHelper (data_list, 5)
    helper.page_count()
    helper.item_count()
    helper.page_index(4)
    helper.page_index(5)
    helper.page_index(-1)
    helper.page_index(40)
    helper.page_item_count(8)
    helper.page_item_count(1)

except IOError: #execption for not finding file
    print("Sorry could not find the file")
except OSError:
    print("File was Found. Error while reading")
except Exception:
    print("Unexpected error occurred")
