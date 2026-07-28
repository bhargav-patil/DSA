n = int(input("Enter number Customer Id "))
Id = []

for i in range(0, n):
    id = int(input("Enter Customer id "))
    Id.append(id)

key = int(input("Enter the Id your searching "))

for i in range(0, len(Id)):
    if Id[i] == key:
        print("Found at postion ", Id[i])
    elif Id[i] == Id[len(Id) - 1]:
        print("Not found")