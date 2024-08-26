def first_zero(arr):
	low,high=0,len(arr)-1
	while low<=high:
		mid=(low+high)//2
		if arr[mid]==0:
			high=mid-1
			if mid==0 or arr[mid-1]==1:
				return mid
		else:
			low=mid+1
	return -1
def count_zeros(arr):
	#print(first_zero(arr))
	if first_zero(arr)==-1:
		return 0
	else:
		zeros=len(arr)-first_zero(arr)
		return zeros

print(count_zeros([1,0,0,0,0,0]))
