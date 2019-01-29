#!/usr/local/bin/python3

#Series 1

#As stated in the instructions, below is a simple list and a prompt for a new
#entry.
print('Series 1')
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print("Here is the current list of fruits:")
print(fruits)
#Here, we ask for a new fruit input.  There's no error correction, so the user
#can input any s, but I suppose that'd be a possibliity unless we checked
#against a list of every possible fruit.
n = str(input("Please enter a new fruit: "))
#Here we're appending the user input to the list above.  If there's another way
#that y'all wanted us to do this I have no idea what it would be.
fruits.append(n)
print(fruits)
#Getting user input for the number in the list to display.
n = int(input("Please enter a number to show the fruit you want: "))
#The -1 is to compensate for the fact that arrays start with 0 and people don't
#think that way.
print(fruits[n-1])
#Here is an example of adding a fruit to the list using addition.
n = str(input("Please enter a new fruit: "))
fruits = [n] + fruits
print(fruits)
#Here is an example of adding a fruit to the list using insert.
n = str(input("Please enter a new fruit: "))
fruits.insert(0,n)
print(fruits)
#This is a forloop to grab anything that starts with P or p.
print('Finding all items that start with P')
newfruit = []
for i in fruits:
    if i.startswith('P'):
        newfruit.append(i)
    elif i.startswith('p'):
        newfruit.append(i)
print(newfruit)

#Series 2
print('')
print('Series 2')
print(fruits)
print('Removing last entry from the fruits list')
#This will always remove the last entry.
fruits2 = fruits
del fruits2[-1]
print(fruits2)
#This is step one of two.  The delete command works.  It is commented so that I
#can work on the bonus section.
#n = str(input("Please enter a fruit to delete (capitalization counts): "))
#fruits2.remove(n)
fruits2 = fruits2 * 2
print(fruits2)
n = str(input("Please enter a fruit to delete (capitalization counts): "))
while True:
    if n in fruits2:
        fruits2.remove(n)
else:
    print('You did not enter a proper fruit')
print(fruits2)
