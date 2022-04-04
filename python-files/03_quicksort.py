def quicksort(arr):
	if len(arr) < 2:
		return arr
	else:
		pivot = arr[0]
		lesser = [i for i in arr[1:] if i <= pivot]
		greater = [i for i in arr[1:] if i > pivot]

		return quicksort(lesser) + [pivot] + quicksort(greater)

print(quicksort([4,2,5,7,3,8,5]))