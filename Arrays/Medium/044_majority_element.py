def majorityElement(array):
    # Write your code here.
    maj = -1
    count = 0
    for num in array:
        if count == 0:
            maj = num
        if num == maj:
            count += 1
        else:
            count -= 1
    return maj


array = [3, 3, 1]
print(majorityElement(array))
