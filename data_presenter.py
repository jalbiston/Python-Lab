open_file = open("CupcakeInvoices.csv")

for cups in open_file:
    print(cups)

open_file.seek(0)

for flavs in open_file:
    flavs = flavs.rstrip('\n').split(',')
    print(flavs[2])

open_file.seek(0)

chocolate = 0
vanilla = 0
strawberry = 0

# for flavs in open_file:
#     flavs = flavs.rstrip('\n').split(',')
#     for total in flavs:
#         if total == "Chocolate":
#             chocolate += 1
#         if total == "Vanilla":
#             vanilla +=1
#         if total == "Strawberry":
#             strawberry += 1



# print("Chocolate", chocolate)
# print("Vanilla", vanilla)
# print("Strawberry", strawberry)

open_file.seek(0)

for line in open_file:
    value = line.rstrip('\n').split(',')
    total = int(value[3]) * float(value[4])
    print(total)
    

open_file.seek(0)


total = 0

for line in open_file:
    value = line.rstrip('\n').split(',')
    total += int(value[3]) * float(value[4])
    
 
print(total)


open_file.close()
