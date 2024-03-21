'''Program to find the largest number in the list
numbers =[3,6,2,8,5,10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)'''

'''
# 2D lists
matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[1][0])'''

# List methods
numbers = [5, 2, 1, 7, 4, 10]
print(numbers)

numbers.insert(0, 6)
print(numbers)

numbers.remove(5)
print(numbers)  # use clear() to empty the list

numbers.pop()  # removes the last number in the list
print(numbers)

print(numbers.index(6))
print(7 in numbers)  # checks for the existence of a number(T or F)

print(numbers.count(1))  # checks the number of times a number appears in the list
numbers.sort()  # Ascending order
numbers.reverse()  # descending order
print(numbers)

numbers2 = numbers.copy()
numbers.append(10)
print(numbers)
print(numbers2)

# program to remove duplicates in a list
figures = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for figure in figures:
    if figure not in uniques:
        uniques.append(figure)
print("")
print(figures)
print(uniques)
