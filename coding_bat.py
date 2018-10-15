'''
Given an array of ints, return the number of 9's in the array.

array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3

'''

'''def array_count9(nums):
#		nine = 0
#		for x in nums:
#			if x == 9:
#				nine += 1
#		return nine

	return nums.count(9)

print (array_count9([1, 9, 9, 3, 9]))'''

###############################################################################

'''Given a string, return the count of the number of times that a substring length 2 appears
in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 
(we won't count the end substring).

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2'''

def last2(str):
	new_str = str[-2:]
	#new_list = str[:-2]
	print (new_str)
	#print (new_list)
	if len(str) < 2:
		return 0
	else:
		return str[:-2].count(new_str) 

print (last2(''))