# Walk through: https://www.youtube.com/watch?v=IcK2Qyk3cUs
# If using python 3, use // as / is true div and returns float
# Search input array 'arr' for specified value 'val'
def binary_search(arr,val):
	# hold the value of the middle of the array
	mid = arr[len(arr)//2]
	if val == mid: return True
	# if the value is less than the middle value, recursive implementation
	# for lower half of the array
	if val < mid: return binary_search(arr[:len(arr)//2], val)
	# if the value is more than the middle value, recursive implementation
	# for upper half of the array
	if val > mid: return binary_search(arr[len(arr)//2+1:], val)

arr = list(range(1000))
print(binary_search(arr, 900))
