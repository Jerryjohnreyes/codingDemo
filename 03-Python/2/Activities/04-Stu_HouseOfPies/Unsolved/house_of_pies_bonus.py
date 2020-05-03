pies = ["Pecan","Apple Crisp","Bean", "Banoffee","Black Bun","Blueberry",
        "Buko", "Burek","Tamale","Steak"]
number_pie_kind =[0]*len(pies)

for i in range(len(pies)):
    print(f"[{i}] {pies[i]}")

another = "y"
number_pies = 0

while another == "y":
    number_pies = number_pies +1
    pie_name = int(input("Enter the number before the pie's kind: "))
    print(f"Great! We'll have that {pies[pie_name]} pie right out for you.")
    number_pie_kind[pie_name] = number_pie_kind[pie_name] + 1
    another = input("Type 'y' if you want to make another order: ")

print(f"You purchased for {number_pies} pies, which are:")
for j in range(len(pies)):
    print(f"{number_pie_kind[j]} {pies[j]}")