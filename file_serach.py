import os



def remove_ext(array):
    for i in range(len(array)):
        array[i] = array[i].split('.')[0]


arr = os.listdir("data/")
print(arr)

remove_ext(arr)
print(arr)