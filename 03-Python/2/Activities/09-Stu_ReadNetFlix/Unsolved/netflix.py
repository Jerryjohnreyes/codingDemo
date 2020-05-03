import os
import csv

csv_path = os.path.join('..', 'Resources','netflix_ratings.csv')
# Set a list where everything is gonna be saved
netflix = []

with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        # Every row is assigned as a list in every entry, listt in a list
        netflix.append(row)

movie = input("What movie are you looking for? ")
found = False

for i in range(len(netflix)):
    if found == False:
        if netflix[i][0] == movie:
            print(f"{movie} is rated {netflix[i][1]} with a rating of {netflix[i][5]}")
            found = True
            break

if found == False:
    print(f"{movie} couldn't be found in our data base.")