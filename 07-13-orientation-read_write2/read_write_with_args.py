
# http://thomas-cokelaer.info/tutorials/python/module_os.html
# For gathering command line input:
import sys
#allows us to check a file to see if it already exists:
import os
# Allows us to pull a random nickname from the list of nicknames, no matter how long the list gets. See 'asign_nicknames' method for where we use this:
from random import randint

# Define some data we want to write to a text file for some reason
nickset = {"The Mooch", "Knuckles", "Burninator", "Kneecap", "Ole Red", "Bubba",
           "OG", "KitKat", "Spanky", "Monkeybutt", "L`il Devil", "Bird Person", "Fancy Slacks"}

nameset = {"Bob Smith", "Charise Anderson", "Jissie David", "Henry Goldberg", "Greg Korte", "Steve Brownlee",
           "Kimmy Bird", "Joe Shepherd", "Emily Lemmon", "Brenda Long", "Harold Brown", "Megan Ducharme", "Darth Vader"}

# 'with' shortcuts opening and closing the file for us. Otherwise we'd have call foo.close() at the end of the read/write action
# Use the os module to check for the nicknames file before writing to it. This allows us to not lose the nicknames added by the 'add_nick' method defined later
with open("data/nicknames.txt", "a") as nicknames:
  # Make sure there's no data before writing (meaning now this only runs the first time app is used)
  if os.path.getsize("data/nicknames.txt") == 0:
    print("Nope, empty", os.path.getsize("data/nicknames.txt"))
    for nick in nickset:
      nicknames.write(nick + '\n')

with open("data/names.txt", "w") as names:
  for name in nameset:
    names.write(name + '\n')


class NameFactory():
  """Represents system for making names and nicknames smooshed together"""

  @staticmethod
  def _get_nicknames():
    """returns a set of nicknames read from a text file"""

    with open("data/nicknames.txt", "r") as nicknames:
      return nicknames.readlines()

  @staticmethod
  def _get_names():
    """returns a set of names read from a text file"""

    with open("data/names.txt", "r") as names:
      return names.readlines()

  def assign_nicknames(self):
    """randomly pairs a nickname with a name. Outputs a list"""

    names = self._get_names()
    nicknames = self._get_nicknames()

    return [f"{name.strip().split(' ')[0]} \"{nicknames[randint(0, len(nicknames)-1)].strip()}\" {name.strip().split(' ')[1]}" for name in names]

  def add_nick(self, new_nick):
    """Allows user to save a new nickname to the existing collection

    Paramters:
      new_nick (String): a nickname passed from command line
    """

    print("new_nick", new_nick)
    with open("data/nicknames.txt", "a") as nickfile:  # "a" arg appends instead of overwriting
      nickfile.write(new_nick + '\n')


if __name__ == '__main__':
  name_maker = NameFactory()

  if len(sys.argv) > 1 and sys.argv[1] == "add_nick":
    name_maker.add_nick(sys.argv[2])
    print("New nickname added. Thanks")
  else:
    print(name_maker.assign_nicknames())
