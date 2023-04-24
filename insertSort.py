import time

print()
# set up to time the code

start_time = time.time()


# ** Insert Sort **


def insertSort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j != 0:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

    return arr


num_list1 = [6, 5, 3, 1, 8, 7, 2, 4] * 1000

# print(insertSort(num_list1))
insertSort(num_list1)

#
end_time = time.time()
# time_elapsed = end_time - start_time
# conver to seconds
# time_elapsed = time_elapsed * 1000
print("time start: ", start_time)
print("Time end: ", end_time)
print("Time elapsed: ", round((end_time - start_time), 2), "sec")
#
#
#
print()
