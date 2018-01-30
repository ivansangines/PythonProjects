# TODO: complete this class
import sys
import copy
class PatientManagement:
    # CONSTRUCTOR WILL REQUEST FOR THE FILE NAME AND INITIALISES ALL THE VARIABLES
    def __init__(self):
        self.patient_dict = {}
        print("Welcome to Patient Management program")
        self.file_name = input("Enter the file Name: ")
        self.read_patients_file(self.file_name)

    # THIS METHOD SHOULD READ DATA FROM FILE AND INTIALISE THE MAIN METHOD

    def read_patients_file(self, file_name):
        try:
            with open(file_name, "r") as file:
                i=0
                for line in file: #for loop to read each line at a time
                    #data = line.split(',') #creating a list with the elements in the line
                    #self.patient_dict[data[0]] = data[1:len(data)] #filling up the dictionary with key as the patient name and value as list of parameters
                    if line[len(line)-1]=="\n": #getting rid of the last element \n of the line
                        self.patient_dict[i]=line[:-1].split(',')
                    else:#the last line does not have \n since it is the last one
                        self.patient_dict[i] = line.split(',')
                    i+=1
            print("Loaded "+str(len(self.patient_dict))+" records from file")
            print("\n")
            self.main_menu()
        except FileNotFoundError:
            print("Sorry the file was not found")
        except OSError:
            print("File was Found. Error while reading")



    """ 
    THIS METHOD SHOULD DISPLAY MAIN MENU AND SHOULD HANDLE ALL THE MENU OPERATIONS
    """

    def main_menu(self):
        print("################################################### \n"
              "#######\t\t\t    MAIN MENU    \t\t\t####### \n"
              "################################################### \n"
              "#######  1.Add Patient\t\t\t\t\t\t####### \n"
              "#######  2.View Patient at index\t\t\t####### \n"
              "#######  3.View all patients\t\t\t\t#######\n"
              "#######  4.Search Patient\t\t\t\t\t####### \n"
              "#######  5.Exit\t\t\t\t\t\t\t\t#######\n"
              "###################################################")
        choice = input("Select your choice: ")#user choses what to do from the menu
        if choice == "1":
            self.add_patient()#calling method
        elif choice == "2":
            print("There are " + str(len(self.patient_dict)) + " patients in the file. "
                                                               "Select an index betwee 0 and " + str(len(self.patient_dict) - 1))
            try:
                index = int(input("Enter patient index: "))#user choses the index to search
                self.find_patient_at_index(index)#calling method at index that the user says
            except ValueError: #whenever the input is not an integer
                print("Invalid index\n")
                index = int(input("Enter patient index: "))
                self.find_patient_at_index(index)#calling method
        elif choice == "3":
            self.show_all()#calling method
        elif choice =="4":
            self.find_patient_with_name()#calling method
        elif choice == "5":
            self.call_exit()#calling method to exit the program
        else: #whenever the input is not between 1-5
            print("Sorry that choice is nor on the menu!\n")
            self.main_menu()




    """ 
    THIS METHOD SHOULD ADD DATA INTO PATIENT DICTONARY
    """

    def add_patient(self):

        name = input("Enter Name to be added: ")
        while name.replace(" ", "").isalpha()==False: #checking if the input is a string
            print("Wrong name, try again")
            name = input("Enter Name to be added: ")
        ssn = input("Enter SSN to be added, (xxx-xxx-xxxx): ")
        while len(ssn) != 12:#checking if it is a proper ssn with length 12
            print("Wrong ssn!")
            ssn = input("Enter SSN to be added, (xxx-xxx-xxxx): ")#if it does not have the proper length, try again
        age_added=False
        while age_added==False:#ask for age untill the user provides a good input
            try:#checking if the input is an integer
                age = int(input("Enter Age to be added: "))
                age_added = True
            except ValueError: #whenever the input is not an int
                print("wrong input, try again!")
            #age = int(input("Enter Age to be added: "))
        diag_added = False
        while diag_added==False: #ask for diagnostic untill the user provides a good input
            try:#checking if the input is an integer
                diag = int(input("Enter Diagnosis to be added: "))
                diag_added=True
            except ValueError:#whenever the input is not an int
                print("wrong input, try again!")

        patient = [name,ssn,age,diag]#creating a patient list with all the info
        self.patient_dict[len(self.patient_dict)] = patient#adding the new patient to the dictionary
        print("Patient added!")
        self.main_menu()#calling menu for further operations



    """ 
    THIS METHOD SHOULD RETRIEVE THE DATA AT SPECIFIED INDEX
    """

    def find_patient_at_index(self, ind_to_returned):
        if ind_to_returned>len(self.patient_dict)-1 or  ind_to_returned<0: #whenever the index is less or higher than the list with all patients
            print("Invalid Index!")
            print("There are " + str(len(self.patient_dict)) + " patients in the file. Select an index betwee 0 and " +
                  str(len(self.patient_dict) - 1))
            index = int(input("Enter patient index: "))#asking to introduce the index again
            self.find_patient_at_index(index)
        else:#whenever we have a correct index
            patient = copy.deepcopy(self.patient_dict[ind_to_returned]) #creating a list using deep copy of the list with the patient info

            print("-----------------------------------------------------\n"
                  "Name\t\t\tSSN\t\t\t\t\tAge\t\t\tDiagnostic\n"
                  "-----------------------------------------------------\n"
                  + str(patient[0]) + "\t\t" + str(patient[1]) + "\t\t" + str(patient[2]) + "\t\t\t" + str(patient[3])) #printing patient info
            self.main_menu()

    """ 
    THIS METHOD SHOULD SHOW ALL RECORDS IN DICTIONARY
    """

    def show_all(self):
        print("-----------------------------------------------------\n"
              "Name\t\t\tSSN\t\t\t\t\tAge\t\t\tDiagnostic\n"
              "-----------------------------------------------------\n")
        for v in self.patient_dict.values(): #for loop through all the values which are lists with each patient info
            patient = copy.deepcopy(v) #coping the list with a patient info in a temporal list
            print(str(patient[0]) + "\t\t" + str(patient[1]) + "\t\t" + str(patient[2]) + "\t\t\t" + str(patient[3])+
                  "\n-----------------------------------------------------\n") #printing each patient at once
        self.main_menu()


    """ 
    THIS METHOD SHOULD RETRIEVE THE RECORD WITH USER NAME
    """

    def find_patient_with_name(self):
        name = input("Enter patient name: ")
        try: #trying to find a key that matches with patient name
            pat_key = [key for key, value in self.patient_dict.items() if value[0].lower() == name.lower()][0] #each value is a list containing all the patients info
                                                                                                               #trying to find a match with the first element of that list which is the name
                                                                                                               #and the input entered
            patient = copy.deepcopy(self.patient_dict[pat_key])#once a matching name is founded in the dic and the key is returned, create a deep copy of the list with patient info
            print("-----------------------------------------------------\n"
                  "Name\t\t\tSSN\t\t\t\t\tAge\t\t\tDiagnostic\n"
                  "-----------------------------------------------------\n"
                  +str(patient[0])+"\t\t"+str(patient[1])+"\t\t"+str(patient[2])+"\t\t\t"+str(patient[3])) #printing the matching patient
            self.main_menu()
        except Exception:#there is no key matching with that name. Means patient is not in Dic
            print("We do not have this patient in our records")
            self.main_menu()



    """ 
    THIS METHOD WRITES NEWLY ADDED DATA INTO TEXT FILE AND EXIT FROM LOOP
    """

    def call_exit(self):
        number_lines =1
        with open(self.file_name, "r") as file:
            for i, line in enumerate(file): #counting the lines in the file
                pass
            number_lines+=i #number of lines is i+1 since 0 based index
            file.close()
        if number_lines<len(self.patient_dict): #means dict has more patients than the file which means we need to pass new patients to the file
            index = len(self.patient_dict) - number_lines
            with open(self.file_name, "a") as file:
                for j in range(len(self.patient_dict)-index,len(self.patient_dict)):
                    line = ','.join(str(x) for x in self.patient_dict[j]) #creating a string using the list of values for each patient
                                                                          #pasing each element to the list to str because .join just works with strings
                    file.write("\n")
                    file.write(line)#writing the new patient to the file
                file.close()
            sys.exit()#exit program
        else:#whenever no patients were added
            sys.exit()





pm = PatientManagement()

