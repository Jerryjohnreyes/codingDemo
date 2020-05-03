import csv
import os

# Three Lists
indexes = [1, 2, 3, 4]
employees = ["Michael", "Dwight", "Meredith", "Kelly"]
department = ["Boss", "Sales", "Sales", "HR"]

# Zip all three lists together into tuples
roster = zip(indexes, employees, department)
print(len(list(roster)[0]))

csvpath = os.path.join('..', 'Resources', 'accounting.csv')
for letter in csvpath:
    print(letter)

# When using list() it makes used the zipped object to be usea as a list

#for item in roster:
#    for sub_item in item:
#        print(sub_item)


# save the output file path
output_file = os.path.join("output.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Index", "Employee", "Department"])

    writer.writerows(roster)


# # to print out to terminal:
# #comment out above code and run the code below
# for employee in roster:
#     print(employee)
