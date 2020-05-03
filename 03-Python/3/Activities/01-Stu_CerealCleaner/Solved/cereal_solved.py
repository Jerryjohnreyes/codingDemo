import os
import csv

cereal_csv = os.path.join("..", "Resources", "cereal.csv")

# Open and read csv
with open(cereal_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile,)
    print(f"Header: {csv_header}")
    #takes away from the original file the header, later from this line
    #the header is no more in the csv.reader object


    # Read through each row of data after the header
    for row in csvreader:
        print(row)
        # Convert row to float and compare to grams of fiber
        if float(row[7]) >= 5:
            print(row)
