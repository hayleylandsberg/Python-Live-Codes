print("Hello, world")

# declare variables
cow = "moo"
dog = "woof"

# if / else / elif
if cow == "moo" and dog == "woof":
  print(cow)
elif cow == "Woof":
  print("WTF?")
else:
  print("The end")

# formatting strings. Both work. First example relies on proper order of your arguments passed to 'format()'
print("A cow says {0}. A dog says {1}".format(cow, dog))
print(f"That's right. I said a cow says {cow}. A dog says {dog}")

# Strings plus other type(s) breaks stuff. No implicit coercion like JS has
num = 3
num_str = "3"
#print( num + num_str) #Throws error
print(str(num) + num_str)  # Throws no error
print(num + int(num_str))  # Throws no error

# collections
# objects and arrays are no more
# lists, tuples, sets, dictionaries

# list
# mylist = [] or list()
junkbox = ["scissors", 3, True, {"key": "value"}]
print(junkbox[1])
junkbox.append("more shit")
print(junkbox)
junkbox.extend([456, False])
# or
junkbox += ["longer", 3.78, "wow!"]
print(junkbox)
del(junkbox[2])

len(junkbox)  # gives you the length of a list
len(cow)  # gives you the length of a string (or the string value held in a variable, like here)

# Slicing is done like this
less_junk = old_list[2:5]
# gives you the 2nd through 4th indexes(so, from index 2 UP TO 5)
# make a clean copy of a list by slicing without index numbers
new_junk = junkbox[:]
# Why not just do new_junk = junkbox ? It doesn't make a NEW list. It just points to the original list. So changing junk would ALSO change junkbox

# set must contain unique items
myset = set() # not {}, because that defaults to a dictionary
unique_list = {"scissors", 3, True}
print(unique_list)
unique_list.add("monkey")
print(unique_list)
unique_list.add(3)
print(unique_list)
unique_list.update("cow", "monkey", 4)

# tuples are immutable
zoo = ("dog", "monkey", "chicken", "bird", "cuttlefish")
print(zoo[3])
zoo_list = list(zoo)
zoo_list.extend(["python", "bat", "mongoose"])
zoo = tuple(zoo_list)
print(zoo)
# del(zoo[3]) Throws error

# dictionaries
foo = {}
foo["name"] = "Fred"
print(foo)

foo["nested_vals"] = {"name": "Larry", "age": 45}
print(foo)
print("nested vals!!!", foo["nested_vals"]["age"])

# loops
for junk in junkbox:
  # cool method: .title() capitalizes the first letter of each word in a string
  print(str(junk).title())

for animal in zoo:
  for junk in junkbox:
    print("I like {0}s and {1}s".format(animal, junk))

# Looping through a dictionary in targeted ways
# for x in foo.keys()
# for x in foo.values()
# for x, y in foo.items() # <— gives you both keys and values(note 2 vars)

# ==========================================================================

# functions
def do_something(foo="monkeys"):
  if foo == "monkeys":
    print("I like " + foo)
    return
  print("Something else " + foo)

do_something("chickens")
do_something()

# joins
listOfStuff = ["animal: cow", "name: Bossie", "age: 25", "color: brown"]
# print((' ... ').join(listOfStuff))

#scope
name = "Fred"

def sayName():
  # uncomment next line to change how scope behaves
  # global name
  name = "Sally"
  print("inside", name)

sayName()
print("outside", name)

def listMyList(stuff, num=5):
  print('This is my list of stuff:')
  for thing in stuff[:num]:
    print(thing)

myList = ["dog", "cat", "monkey", "fish", "rabbit", "orca", "hamster"]
listMyList(myList)
listMyList(myList, 3)

if __name__ == "__main__":
  print("Only runs if module is executed directly", (' ... ').join(listOfStuff))
