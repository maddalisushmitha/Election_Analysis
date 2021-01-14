
import os
import csv
# # Using indirect Path to Assign a variable for the file to load and the path
# file_to_load = os.path.join("Resources","election_results.csv")
# #Opening election_results file in read mode
# with open(file_to_load) as election_data:
#     # Print the file object
#     print(election_data)
#---------------------------------------------------------------------------------------------------------
# #Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# with open(file_to_save, "w") as txt_file:
# # Write some data to the file.
#     txt_file.write("Counties in the Election\n")
#     txt_file.write("------------------------\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")
# #-------------------------------------------------------------------------------------------------------
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)
     # Print the header row.
    headers = next(file_reader)
    print(headers)