# 	Write a Python program to find number of vow vowels in a list the list should be content the name of the student in a class.
def count_vowels(name):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    # Iterate through each character in the name
    for char in name:
        if char in vowels:
            vowel_count += 1

    return vowel_count

def total_vowels_in_class(names):
    total_vowels = 0

    # Iterate through each name in the list
    for name in names:
        total_vowels += count_vowels(name)

    return total_vowels

# Example usage:
class_names = ["Alice", "Bob", "Charlie", "David"]
total_vowels = total_vowels_in_class(class_names)
print("Total number of vowels in the class names:", total_vowels)
