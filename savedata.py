import pickle
import os
os.system("clear")

# Create a list
names = ["Anita","Tim","Mick","Clint","Dim"]

# Print the list
print ("Original names")
print (names)

# Save the list
pickle.dump(names, open("names.txt", "wb"))

# Change
names.remove("Mick")

# Print the list
print ("Changed names")
print (names)

# Load the list
names = pickle.load(open("names.txt", "rb"))

# Print the list
print ("Loaded names")
print (names)
