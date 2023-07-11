import numpy

def arrays(arr):
    array_forward = numpy.array(arr, float)
    # print(array_forward)
    return (numpy.flip(array_forward))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)