def take_input():
    num = int(input("Enter a number (negative to stop):- "))


    if num < 0:
        print("Negative number has been entered. The recursion will be stopping.")
        return
    take_input()  # Recursively call the function again and again.


# Start the recursive input.
take_input()