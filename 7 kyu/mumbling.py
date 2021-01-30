def accum(s):
    arr = [char for char in s]

    for i in range(1,len(arr)):
        arr[i] *= i+1

    return "-".join(char.capitalize() for char in arr)