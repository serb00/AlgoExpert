def longestPeak(array):
    # Write your code here.
    peak, maxPeak = 0, 0
    if len(array) < 3:
        return 0
    for i in range(1, len(array) - 1):
        if array[i - 1] < array[i] > array[i+1]:
            peak = 3
            step = 2
            while i - step >= 0 and array[i-step] < array[i-step+1]:
                peak += 1
                step += 1
            step = 2
            while i + step < len(array) and array[i+step] < array[i+step-1]:
                peak += 1
                step += 1
            maxPeak = max(maxPeak, peak)

    return maxPeak


array = [1, 2, 3, 4, 5, 1]
print(longestPeak(array))
