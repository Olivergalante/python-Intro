numbers = [1, 2, 3, 4, 5, 99, 2600, 300]
number1 = list(reversed(numbers))
print(number1)

thing = "hellos"
my_list = []
for x in thing:
  my_list.append(x)
print(my_list)

rev = list(reversed(my_list))
print(rev)

empty_string = " "

for x in rev: 
  empty_string += (x)
print(empty_string)