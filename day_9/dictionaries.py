#dictionary = {key: value}
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

#retrieving an item form the dictionary - dictionary[key]
print(programming_dictionary["Function"])

#adding a piece of data to the dictionary - dictionary[key] = value
programming_dictionary["Loop"] = "The action of doing something over and over again"
#print(programming_dictionary)

#creating an empty dictionary - dictionary = {}
#wiping an existing dictionary is the same as creating an empty dictionary - dictionary = {}
#programming_dictionary = {}
#print(programming_dictionary)

#editing an item in a dictionary
programming_dictionary["Bug"] = "An error."
#print(programming_dictionary)

#looping through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


