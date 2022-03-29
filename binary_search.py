def binary_search(arr, item):
	'''
	Returns the position of the item in the array if it exists.
	Else returns `None`.
	'''

	low = 0
	high = len(arr) - 1
	while low <= high:
		mid = (low + high) // 2
		guess = arr[mid]
		if guess == item:
			return mid
		if guess < item:
			low = mid + 1
		elif guess > item:
			high = mid - 1
	return None

# make sure the list is sorted
my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3)) # => 1
print(binary_search(my_list, -1)) # => None