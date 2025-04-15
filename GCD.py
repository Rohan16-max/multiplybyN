smallest = int(input("Enter the smallest number:-"))
biggest = int(input("Enter the biggest number:-"))

while(smallest):
    numstore = smallest
    smallest = biggest % smallest
    biggest = numstore

print("GCD is ",biggest)