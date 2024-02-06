# Consider a file number.txt with some numbers. write a python program to read the numbers from number.txt, save the even numbers into even.txt and odd numbers into odd.txt.
def separate_numbers(input_filename, even_filename, odd_filename):
    try:
        with open(input_filename, 'r') as input_file, \
             open(even_filename, 'w') as even_file, \
             open(odd_filename, 'w') as odd_file:
            
            # Read numbers from input file
            numbers = input_file.readlines()

            # Iterate through each number
            for number in numbers:
                num = int(number.strip())
                # Check if the number is even or odd
                if num % 2 == 0:
                    even_file.write(f"{num}\n")  # Write even number to even file
                else:
                    odd_file.write(f"{num}\n")   # Write odd number to odd file
            
            print("Numbers separated into even.txt and odd.txt successfully.")
    
    except FileNotFoundError:
        print("File not found. Make sure the input file exists.")

# File names
input_filename = "numbers.txt"
even_filename = "even.txt"
odd_filename = "odd.txt"

# Call the function to separate numbers
separate_numbers(input_filename, even_filename, odd_filename)
