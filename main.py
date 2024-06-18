import time

def fibonacci2(n):
  fibNumbers = [0, 1]  # List of first two Fibonacci numbers
  # Now append the sum of the two previous numbers to the list
  for i in range(2, n + 1):
      fibNumbers.append(fibNumbers[i - 1] + fibNumbers[i - 2])
  return fibNumbers[n]

# Test the function
n = 10  # Replace with the desired value of n

# Time the function for n = 10
startTime1 = time.perf_counter()  # Start the timer
result = fibonacci2(n)
endTime1 = time.perf_counter()  # Stop the timer

print(f"The {n}-th Fibonacci number is: {result}")
print(f"Execution time for n = 10: {endTime1 - startTime1} seconds")

n = 20  # Replace with the desired value of n

# Time the function for n = 20
startTime2 = time.perf_counter()  # Start the timer
result = fibonacci2(n)
endTime2 = time.perf_counter()  # Stop the timer

print(f"The {n}-th Fibonacci number is: {result}")
print(f"Execution time for n = 20: {endTime2 - startTime2} seconds")