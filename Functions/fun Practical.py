### 1. **Function to Sum All Even Numbers in a List:**

def sum_even_numbers(lst):
    return sum(num for num in lst if num % 2 == 0)

   # Example usage
numbers = [1, 2, 3, 4, 5, 6]
print(sum_even_numbers(numbers))  # Output: 12
   

### 2. **Function to Reverse a String:**
 
def reverse_string(s):
    return s[::-1]

   # Example usage
print(reverse_string("Hello"))  # Output: "olleH"
  

### 3. **Function to Return the Square of Each Number in a List:**
   
def square_numbers(lst):
    return [num ** 2 for num in lst]

   # Example usage
numbers = [1, 2, 3, 4]
print(square_numbers(numbers))  # Output: [1, 4, 9, 16]
   

### 4. **Function to Check if a Number is Prime from 1 to 200:**
   
def is_prime(num):
   if num < 2:
        return False
   for i in range(2, int(num**0.5) + 1):
       if num % i == 0:
               return False
       return True

   primes = [num for num in range(1, 201) if is_prime(num)]
   print(primes)  # Output: List of prime numbers from 1 to 200
 

### 5. **Iterator Class for Fibonacci Sequence:**
  
   class FibonacciIterator:
       def __init__(self, n_terms):
           self.n_terms = n_terms
           self.a, self.b = 0, 1
           self.count = 0

       def __iter__(self):
           return self

       def __next__(self):
           if self.count < self.n_terms:
               result = self.a
               self.a, self.b = self.b, self.a + self.b
               self.count += 1
               return result
           else:
               raise StopIteration

   # Example usage
   fib_iter = FibonacciIterator(10)
   for num in fib_iter:
       print(num, end=" ")  # Output: 0 1 1 2 3 5 8 13 21 34


### 6. **Generator Function for Powers of 2:**
   
   def powers_of_2(exponent):
       for i in range(exponent + 1):
           yield 2 ** i

   # Example usage
   for power in powers_of_2(5):
       print(power, end=" ")  # Output: 1 2 4 8 16 32
 

### 7. **Generator Function to Read File Line by Line:**
  
   def read_file_line_by_line(file_name):
       with open(file_name, 'r') as file:
           for line in file:
               yield line.strip()

   # Example usage
   # for line in read_file_line_by_line('example.txt'):
   #     print(line)


### 8. **Lambda Function to Sort List of Tuples by Second Element:**

   tuples_list = [(1, 3), (4, 1), (2, 5), (3, 2)]
   sorted_list = sorted(tuples_list, key=lambda x: x[1])

   # Output: [(4, 1), (3, 2), (1, 3), (2, 5)]
   print(sorted_list)


### 9. **Program to Convert List of Temperatures from Celsius to Fahrenheit Using `map()`:**
  
   celsius = [0, 20, 37, 100]
   fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

   # Output: [32.0, 68.0, 98.6, 212.0]
   print(fahrenheit)
 

### 10. **Program to Remove All Vowels from a String Using `filter()`:**
   
   def remove_vowels(s):
       vowels = "aeiouAEIOU"
       return ''.join(filter(lambda char: char not in vowels, s))

   # Example usage
   print(remove_vowels("Hello World"))  # Output: "Hll Wrld"
  

### 11. **Accounting Routine Using Lambda and `map()` to Return List of 2-Tuples:**
#   Given a list with sublists, where each sublist contains an order number, price per item, and quantity, we want to return a list with tuples consisting of the order number and the total price (price per item * quantity). If the total price is less than 100, we add an extra 10 euros.

  # **Example Input**:
  
   orders = [
       [34587, 4.50, 10],
       [98762, 5.00, 3],
       [77226, 2.30, 5],
       [88112, 7.20, 1]
   ]

   result = list(map(lambda x: (x[0], x[1] * x[2] if x[1] * x[2] >= 100 else x[1] * x[2] + 10), orders))

   # Output: [(34587, 45.0), (98762, 25.0), (77226, 21.5), (88112, 17.2)]
   print(result)