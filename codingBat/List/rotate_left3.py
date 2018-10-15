'''
rotate_left3

Given an array of ints length 3,
return an array with the elements
"rotated left" so {1, 2, 3} yields {2, 3, 1}.

rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]
'''


def rotate_left3(nums):
    # str(nums)
    return nums[1:] + nums[:1]


print(rotate_left3([1, 2, 3]))


'''
Given an array of ints length 3, figure out which is larger,
the first or last element in the array, and set all the other
elements to be that value. Return the changed array.

max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]

'''


def max_end3(nums):

	''' second_int = nums[(len(nums)-1)]

    bigger_int = max(nums[0], second_int)

    new_list = []

    while len(new_list) != 3:
        new_list.append(bigger_int)

    return new_list'''
	m = max(nums[0], nums[2])
	return [m, m, m]

print(max_end3([11, 2, 1]))

'''
Return an int array length 3 containing the first 3
digits of pi, {3, 1, 4}.

make_pi() → [3, 1, 4]
'''

def make_pi():
	return [3, 1, 4]
print (make_pi())


'''
make_ends

Given an array of ints, return a new array length 2 containing
the first and last elements from the original array. The original
array will be length 1 or more.

make_ends([1, 2, 3]) → [1, 3]
make_ends([1, 2, 3, 4]) → [1, 4]
make_ends([7, 4, 6, 2]) → [7, 2]

'''

def make_ends(nums):
	return [nums[0], nums[-1]]

print (make_ends([1, 2, 3]))


def sum2(nums):
  if len(nums) == 0:
    return 0
  elif len(nums) <= 2:
    return sum(nums)
  else:
    return nums[0] + nums[1]

print (sum2([1,2,3]))