import time
def quick(arr):
	if len(arr)< 2:
		return arr
	pivot = arr[0]
	less = [i for i in arr[1:] if i <= pivot ]

	greater = [i for i in arr[1:] if i > pivot]

	return quick(less) + [pivot] + quick(greater)

def quicksort(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)
    return myList
def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right

myarr = [35,10,5,6,7,5,988,2,3]
quiktime = time.time()
print(quick(myarr))
oy =quiktime-time.time()
left = 0
right = len(myarr) - 1
quiky = time.time()
print(quicksort(myarr,left, right))
aye= quiky-time.time()


if oy> aye:
	print("fake quicksort slower")

else:
	print("easier quicksort faster")
print(oy)
print(aye)

