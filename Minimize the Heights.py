def getMinDiff(arr, n, k):
	arr.sort()
	ans = arr[n - 1] - arr[0] 

	tempmin = arr[0]
	tempmax = arr[n - 1]

	for i in range(1, n):
		if arr[i] < k:
			continue
		tempmin = min(arr[0] + k, arr[i] - k)

		tempmax = max(arr[i - 1] + k, arr[n - 1] - k)

		ans = min(ans, tempmax - tempmin)

	return ans



k = 6
n = 3
arr = [1,15,10]
ans = getMinDiff(arr, n, k)
print(ans)


