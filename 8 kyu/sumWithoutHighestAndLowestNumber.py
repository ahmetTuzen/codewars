def sum_array(arr):
    return 0 if arr is None else sum(arr) - max(arr) - min(arr) if len(arr) > 1 else 0
