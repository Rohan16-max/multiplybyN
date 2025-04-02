# Function 1: Multiply using a loop 
def multiply_using_iteration(N, M):
    result = 0
    for _ in range(M):
        result += N
    return result

# Function 2: Multiply using N iterations 
def multiply_using_N_iterations(N, M):
    result = 0
    for _ in range(N):
        result += M
    return result

# Main function to demonstrate both methods
def main():
    N = int(input("Enter the value for N: "))
    M = int(input("Enter the value for M: "))
    
    # Using iteration-based multiplication
    result_1 = multiply_using_iteration(N, M)
    print(f"Result using iteration-based multiplication:- {result_1}")
    
    # Using N iterations 
    result_2 = multiply_using_N_iterations(N, M)
    print(f"Result using N iterations :- {result_2}")

# Run the program
if __name__ == "__main__":
    main()
