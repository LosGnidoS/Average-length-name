#!/usr/bin/python3
#created by Kirill Shvedov
#Average length of names in []

names = ["John", "Kirill", "James", "Andrew", "Dasha", "Parker"]
result = 0
for name in names:
	print(len(name))

# summing up the length of each element in []
x = (len(names[0])+len(names[1])+len(names[2])+
	len(names[3])+len(names[4])+len(names[5]))

print(x)
average = x/len(list(name))
print(int(average))

#def print_average(arr):
#	print(0 if not arr else sum(arr) / len(arr))






