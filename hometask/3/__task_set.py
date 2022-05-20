# Write a Python program to check if two given sets have no elements in common.

x = {1, 2, 3, 4}
y = {4, 5, 6, 7}
z = {8}
print("Original set elements:")
print(x)
print(y)
print(z)

print("\nConfirm two given sets have no element(s) in common:")
print("\nCompare x and y: ")
print(x.isdisjoint(y))
print("\nCompare x and z: ")
print(z.isdisjoint(x))
print("\nCompare y and z: ")
print(y.isdisjoint(z))

# Write a Python program to remove the intersection of a 2nd set from the 1st set.

sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Original sets:")
print(sn1)
print(sn2)

print("\nRemove the intersection of a 2nd set from the 1st:")
sn1.difference_update(sn2)
print("sn1: ", sn1)
print("sn2: ", sn2)
