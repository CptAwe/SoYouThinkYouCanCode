"""
This is an example to show how usefull (or not!) is to create
objects by reference in python
"""

# Lets create a dictionary like this one:
# a = {
#     "dog" : {
#         "name" : "Boobis",
#         "eats" : ["meat", "treats", "anything that smells great"]
#     },
#     "cat" : {
#         "name" : "Logan",
#         "eats" : ["meat", "fish", "Boobis' food"]
#     },
#     # ....
# }
# For a lot of animals


kinds_of_animals = ["dog", "cat", "elephant", "fish"]
animal_information = {
    "name" : "",
    "eats" : []
}

animals = dict(zip(
    kinds_of_animals,
    [animal_information]*len(kinds_of_animals)
))


animals["dog"]["name"] = "Boobis"

print(animals)

# All the animals' names are now "Boobis" because
# the animal_information dictionary is passed by reference
