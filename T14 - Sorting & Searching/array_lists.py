"""
hyperiondev - Software Engineering (Fundamentals)
Task 14 - "Sorting and Searching"
Author: Helder P - HP24010013265
Date: 30/03/2024

Description: (Auto-graded) Practical Task 1 - "array_lists.py"
"""

class Album:
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"

# Creating albums1 list
albums1 = [
    Album("Abbey Road", 17, "The Beatles"),
    Album("Thriller", 9, "Michael Jackson"),
    Album("Back in Black", 10, "AC/DC"),
    Album("The Dark Side of the Moon", 10, "Pink Floyd"),
    Album("Rumours", 11, "Fleetwood Mac")
]

# Printing albums1 list
print("Albums1:")
for album in albums1:
    print(album)

# Sorting albums1 list by number_of_songs
albums1.sort(key=lambda x: x.number_of_songs)

# Printing sorted albums1 list
print("\nSorted Albums1 by number of songs:")
for album in albums1:
    print(album)

# Swapping elements at position 1 and 2 in albums1
albums1[1], albums1[2] = albums1[2], albums1[1]

# Printing albums1 after swapping
print("\nAlbums1 after swapping:")
for album in albums1:
    print(album)

# Creating albums2 list
albums2 = []

# Adding five albums to albums2
albums2.extend([
    Album("Born to Die", 12, "Lana Del Rey"),
    Album("Nevermind", 13, "Nirvana"),
    Album("21", 11, "Adele"),
    Album("The Wall", 26, "Pink Floyd"),
    Album("Led Zeppelin IV", 8, "Led Zeppelin")
])

# Printing albums2 list
print("\nAlbums2:")
for album in albums2:
    print(album)

# Copying albums from albums1 to albums2
albums2.extend(albums1)

# Adding new albums to albums2
albums2.extend([
    Album("Dark Side of the Moon", 9, "Pink Floyd"),
    Album("Oops!... I Did It Again", 16, "Britney Spears")
])

# Sorting albums2 alphabetically by album name
albums2.sort(key=lambda x: x.album_name)

# Printing sorted albums2 list
print("\nSorted Albums2 by album name:")
for album in albums2:
    print(album)

# Searching for "Dark Side of the Moon" in albums2
search_album = "Dark Side of the Moon"
index = None
for i, album in enumerate(albums2):
    if album.album_name == search_album:
        index = i
        break

if index is not None:
    print(f"\n'{search_album}' found at index {index} in Albums2.")
else:
    print(f"\n'{search_album}' not found in Albums2.")
