# # # 	Write a program counting the number of elements in the list without using length function.
# # def count_elements(lst):
# #     count = 0  # Initialize counter to 0

# #     # Iterate through the list and increment the counter for each element
# #     for _ in lst:
# #         count += 1

# #     return count

# # # Example usage:
# # my_list = [1, 2, 3, 4, 5, 6,0, 7]
# # print("Number of elements in the list:", count_elements(my_list))



list = []
num = int(input("Enter the number of elements :"))
for i in range(num):
    
    print("Enter the elements of array :")
    list.append(input())
print(list)
# list = [12,3,4,57,86]
length = 0
for i in list:
    length = length +1
print("Number of elements are:", length)

