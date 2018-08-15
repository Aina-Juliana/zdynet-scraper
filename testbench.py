from zdynet import getAllTitles

# Get the list of All Characters
characterList = getAllTitles('http://marvelcinematicuniverse.wikia.com/wiki/Category:Characters')

for character in characterList:
    print(character)
