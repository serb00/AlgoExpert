def majorityElement(array):
    # Write your code here.
    maj = -1
    count = 0
    for i in range(len(array)):
        if count == 0:
            maj = array[i]
        if array[i] == maj:
            count += 1
        else:
            count -= 1
    return maj


array = [3, 3, 1]
print(majorityElement(array))
