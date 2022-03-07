import pandas as pd


# Using Pandas library
# Prompt user to enter the file name
file_name = input("Name the file - ").title()

# imported xlsx file with help of pandas library and stored it in new_dataframe_1
input_dataframe = pd.read_excel(f"{file_name}.xlsx")

# No of students
no_of_students = len(input_dataframe.index)

# Created a function as it is used many times
# it takes the dataframe data_file and removes the column at the position "a"
# and inserts it in the column "b"

# Deletes columns in one Dataframe and inserts it into another
def insert_column(a,data_file_1, dat_file_2):
    length_of_dataframe = len(dat_file_2.columns)
    required_column = data_file_1.columns[a]
    column_data = data_file_1.pop(required_column)
    dat_file_2.insert(length_of_dataframe, required_column,column_data)

no_of_tests = 0
no_of_concept_tests = 0
no_of_full_chapter_test = 0
no_of_topic_tests = 0

# Used to find out how many different types of tests performed
for i in range(3, len(input_dataframe.columns), 6):
    no = input_dataframe.iloc[:,i].name
    no_of_tests+=1
    if "C" in no[0]:
        no_of_concept_tests+=1
    elif "F" in no[0]:
        no_of_full_chapter_test+=1
    else:
        no_of_topic_tests+=1

# Creates sorted data frame
new_dict_1 = {}
new_dataframe_1 = pd.DataFrame(new_dict_1)
for i in range(3):
    insert_column(0, input_dataframe, new_dataframe_1)

# This function helps to sort the tests in order
def inserts_tests(a, b, data_file_1, dat_file_2):
    for i in range(a+1):
        for j in range(len(data_file_1.columns)):
            no = data_file_1.iloc[:,j].name
            if b in no and str(i) in no:
                for _ in range(6):
                    insert_column(j,data_file_1, dat_file_2)
                break

inserts_tests(no_of_concept_tests,"Concept",input_dataframe, new_dataframe_1)
inserts_tests(no_of_full_chapter_test,"Full", input_dataframe, new_dataframe_1)
inserts_tests(no_of_topic_tests,"Topic", input_dataframe, new_dataframe_1)

# created a Dictionary with headings in the required output as the keys and it's values as empty lists.
outputdata = {"Name":[], "Username": [], "Chapter Tag":[], "Test_Name":[], "score":[],"time-taken(seconds)":[],
"answered":[], "correct":[], "wrong":[], "skipped":[]}

# output_heads is the list of outputdata keys
output_heads = list(outputdata.keys())

# the below for loop appends data to the values for each key in the output data
for i in range(no_of_students):
    present_list = new_dataframe_1.loc[i]
    # the below for loop appends the first four colums to the outputdata 9 times for each
    # as there are total of nine tests performed
    for j in range(no_of_tests):  
        for k in range(3):
            present_index = output_heads[k]        
            present_index_value = outputdata[present_index] 
            present_index_value.append(present_list[k])
        if j<=no_of_concept_tests-1:
            present_index = output_heads[3]
            present_index_value = outputdata[present_index]
            present_index_value.append(f"Concept Test {j+1}")
        elif j<=no_of_concept_tests+no_of_full_chapter_test-1:
            present_index = output_heads[3]
            present_index_value = outputdata[present_index]
            present_index_value.append(f"Full Chapter Test {j-4}")
        else:
            present_index = output_heads[3]
            present_index_value = outputdata[present_index]
            present_index_value.append(f"Topic Test {j-6}")
    # The below for loop appends all the other colums for the required output
    for k in range(4,10):
        present_index = output_heads[k]
        present_index_value = outputdata[present_index]
        for j in range(0,9):
            present_index_value.append(present_list[k+(j*6)-1])

# Created a dataframe with the outputdata and stored it in output_dataframe
output_dataframe = pd.DataFrame(outputdata)

new_dict_2={}
new_dataframe_2 = pd.DataFrame(new_dict_2)

# Creating a func to make it an ordered Dataframe
def arrange_column(a):
    req_col = output_dataframe.columns.get_loc(a)
    insert_column(req_col, output_dataframe, new_dataframe_2)

output_keys_order = ["Name", "Username", "Chapter Tag", "Test_Name", "answered", "correct",
 "score", "skipped", "time-taken(seconds)", "wrong"]

# Creates a desired Dataframe
for i in range(len(output_keys_order)):
        arrange_column(output_keys_order[i])

# Below lines deletes the rows which are not performed by the student
new_dataframe = new_dataframe_2.loc[new_dataframe_2["answered"]!="-"]
new_dataframe.dropna()

# Asks how do you want to save the file
file_save = input("Name of the file_name to be saved as - ").title()

# Creates the excel file with ,xlsx extension and does'nt add the index
new_dataframe.to_excel(f"{file_save}.xlsx", sheet_name="Output_Task-2", index=False)