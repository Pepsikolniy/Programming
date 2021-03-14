def create(length, first_num = 0, step = 0):
    return [i for i in range(first_num, first_num + step*length, step)]

def sort(arr, length):
    for i in range(1, length):
        temp = arr[i]
        j = i-1
        while j >=0 and temp < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    return arr

_print = print
def print(array, length):
    _print (array)

length = int(input())
first_num = int(input())
step = int(input())
arr = create(length, first_num, step)
sort(arr, length)
print(arr, length)
