# 1. Populating a dictionary
# Create a dictionary by using all the given variables.

first_name = 'John'
last_name = 'Doe'
favorite_hobby = 'Python'
sports_hobby = 'gym'
age = 82
# Your implementation
my_dictionary = dict(
    first_name="John",
    last_name="Doe",
    favorite_hobby= "Phyton",
    sports_hobby = "gym",
    age="82"
)
print("Created dictionary is:")
print(my_dictionary)


# assert my_dict == {
#         'name': 'John Doe',
#         'age': 82,
#         'hobbies': ['Python', 'gym']
    # }

# 2. Accessing and merging dictionaries
# Combine dict1, dict2, and dict3 into my_dict. In addition, get the value of special_key from my_dict into a special_value variable.
# Note that original dictionaries should stay untouched and special_key should be removed from my_dict.

dict1 = dict(
    key1='This is not that hard',
    key2='Python is still cool')

dict2 = {'key1': 123,
         'special_key': 'secret'}

# This is also a away to initialize a dict (list of tuples)
dict3 = dict(
    [('key2', 456),
     ('keyX', 'X')])

# 'Your impelementation'
def mergeDict(dict1, dict2):
    my_dict = {**dict1, **dict2}
    for key, value in my_dict.items():
        if key in dict1 and key in dict2:
            my_dict[key] = [value, dict1[key]]
            return my_dict
my_dict_new = mergeDict(dict3, mergeDict(dict1, dict2))
for key, value in my_dict_new.items():
    if key == "special_key":
        special_value = my_dict_new.get('special_key')
print("Special value: " + special_value)
my_dict_new.pop('special_key', None)
print(my_dict_new)

# assert my_dict == {'key1': 123, 'key2': 456, 'keyX': 'X'}
# assert special_value == 'secret'

# Let's check that the originals are untouched
assert dict1 == {
        'key1': 'This is not that hard',
        'key2': 'Python is still cool'
    }
assert dict2 == {'key1': 123, 'special_key': 'secret'}
assert dict3 == {'key2': 456, 'keyX': 'X'}