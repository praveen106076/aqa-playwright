# list1 = [2,4,15,6,9,12]

## Adding all elements
# sum = 0
# for x in list1:
#     sum += x
#
# print(sum)

## multiplying all elements
# sum = 1
# for x in list1:
#     sum *= x
#
# print(sum)

## find largest
#
# list1.sort()
#
# print(list1[-1])

# find smallest

# list1.sort()
#
# print(list1[0])

## find largest another

# def find_largest(list1):
#     max1 = list1[0]
#     for i in list1:
#         if i > max1:
#             max1 = i
#
#     return max1
# print(find_largest(list1))

## find smallest another

# def find_largest(list1):
#     max1 = list1[0]
#     for i in list1:
#         if i < max1:
#             max1 = i
#
#     return max1
# print(find_largest(list1))

# count for first and last char same

# list2 = ['abc', 'xyz', 'aba', '1221']
#
# def find_first_and_last_char(list2):
#     count = 0
#     for i in list2:
#         if i[0] == i[-1]:
#             count += 1
#     return count
#
# print(find_first_and_last_char(list2))

# tuples last element sorted

# def last(t1):
#     return t1[-1]
#
# def sort_list_last(t1):
#     t1 = sorted(t1, key=last)
#     return t1
#
# print(sort_list_last([(2, 5), (1, 7, 2), (4, 4), (2, 3), (2, 1)]))

# remove duplicates

# a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
#
# uniq_elements = []
# dup_elements = set()
#
# for i in a:
#     if i not in dup_elements:
#         uniq_elements.append(i)
#         dup_elements.add(i)
#
# print(dup_elements)
# print(uniq_elements)

# Is Prime

