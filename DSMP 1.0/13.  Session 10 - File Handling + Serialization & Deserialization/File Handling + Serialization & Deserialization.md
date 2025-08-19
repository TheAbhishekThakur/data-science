# File Handling + Serialization & Deserialization

## Types of data used for I/O
- `Text`: '12345' as a sequence of unicode chars
- `Binary`: 12345 as a sequence of bytes of it's binary equivalent

## Here there are 2 file types to deal with:
- `Text Files`: All programs files are text files
- `Binary Files`: Images, Music, Video, EXE files

## How file I/O id done in most programming languages
- Open a file
- Read/Write data
- Close the file

## How exactly open() works?
- Python checks if the file exists (for reading).
- It opens a connection (file descriptor) to the file.
- If opening for writing and the file doesn’t exist, it creates it.
- The file object manages reading/writing and buffering.
- When you’re done, closing the file releases system resources.


## Problem with "w" mode
### 1. Accidental Data Loss:
If you open an existing file in "w" mode, all its previous contents are erased. This can lead to accidental data loss if you meant to add to the file instead of overwriting it.

### 2. Cannot Read:
You cannot read from a file opened in "w" mode. If you try f.read(), you’ll get an error.

### 3. File Not Created in Non-Existent Directory:
If you specify a path to a directory that doesn’t exist, Python will raise a FileNotFoundError.


## Using Context Manager (With)
- It's a good idea to close a file after usage as it will free up.
- If we don't close it, garbage collector would close it.
- `with` keyword closes the file as soon as the usage is over.


## Problems with working in text mode
- Can't work with binary files like images
- Not good for other data types like int/float/list/tuples


# Serialization and Deserialization

`Serialization`: Process of converting python data types to JSON format.

`Deserialization`: Process of converting JSON to python data types.


# Pickling

`Pickling` is the process whereby a Python object hierarchy is converted into a byte system.

`Unpickling` is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy.

## Pickling Vs JSON
Pickle lets the user to store data in binary format. JSON lets the user store the data in a human-readable text format.