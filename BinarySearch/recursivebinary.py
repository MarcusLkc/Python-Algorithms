def binary_search(list, item, low=0,high=None):
	
	high = len(list) if high is None else high

	
	mid = (low + high)//2
	guess = list[mid]
	if guess == item:
		return mid
	if guess > item:
		return binary_search(list, item, low, mid-1)
	else:
		return binary_search(list, item, mid+1, high)
	

my_list = [1,2,3,4,8,30]

print(binary_search(my_list,30))
