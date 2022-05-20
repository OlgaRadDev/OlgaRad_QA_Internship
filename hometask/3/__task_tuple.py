# Write a Python program calculate the product, multiplying all the numbers of a given tuple.
# Original Tuple:

nums = (4, 3, 2, 2, -1, 18)
def prod(value):
    res = 1
    for item in value:
        res *= item
    return res

result = prod(list(nums))
print(result)

#Product - multiplying all the numbers of the said tuple: -864
# assert result == -864

# Write a Python program to convert a tuple of string values to a tuple of integer values.
# Original tuple values:
nums = (('333', '33'), ('1416', '55'))
def convert_tuple_int(nums):
    result = tuple((int(x[0]), int(x[1])) for x in nums)
    return result
res = convert_tuple_int(nums)
result5 = tuple((int(x[0]), int(x[1])) for x in nums)

print(result5)

# result =
# assert result == ((333, 33), (1416, 55))

# Write a Python program to convert a given tuple of positive integers into an integer.
# Original tuple:
original1 = (1, 2, 3)

result1 = int(''.join(map(str, original1)))
print(result1)

# assert result == 123

original2 = (10, 20, 40, 5, 70)

result2 = int(''.join(map(str, original2)))
print(result2)

assert result == 102040570