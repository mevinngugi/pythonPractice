'''
Given 2 strings, return their concatenation,
except omit the first char of each.
The strings will be at least length 1.

non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava
'''

def non_start(a, b):
	if len(a) == 1 and len(b) > 1:
		a = ''
		return a + b[1 :]
	elif len(a) > 1 and len(b) == 1:
		b = ""
		return a[1 :] + b
	elif len(a) == 0 and len(b) == 0:
		return None
	else:
		return a[1 :] + b[1 :]
		#return True

print(non_start('H', 'There'))