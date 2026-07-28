n = int(input("Enter number Customer Id "))
Id = []

for i in range(0, n):
    id = int(input("Enter Customer id "))
    Id.append(id)

key = int(input("Enter the Id your searching "))

for i in range(0, len(Id)):
    if Id[i] == key:
        print("Found at postion ", i+1)
        break
else:
    print("Not found")