# 	Write a program to delete the duplicate number from array

list = []
num = int(input("Enter length of array :"))
for i in range(num):
    print("Enter element :", end = '')
    list.append(int(input()))
print(list)
new_list = set(list)
print(new_list)
