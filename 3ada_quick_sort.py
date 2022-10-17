def partition(array, low, high):     #fun to find partition position
    pivot = array[high]                                       # choose right most element as pivot
    i = low - 1                          #pointer for  element 

    for j in range(low, high):
        if array[j] <= pivot:                        # if element smaller than pivot is found,swap it swap it with the greater element pointed by i
          i = i + 1                                                
          (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def quickSort(array, low, high):                  # function to perform quicksort
  if low < high:
    pi = partition(array, low, high)

    quickSort(array, low, pi - 1)                  #recursive call on the left of the povit

    quickSort(array, pi + 1, high)              #recursive call on the right  of the pivot
 

data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

quickSort(data, 0, len(data) - 1)

print('Sorted Array in Ascending Order:')
print(data)