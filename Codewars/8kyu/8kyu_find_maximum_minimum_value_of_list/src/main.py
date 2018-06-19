def mysolution_min(arr):
    return sorted(arr)[0]

def mysolution_max(arr):
    return sorted(arr)[-1] 

# ------------------------------

def othersolution_min(arr):
    return min(arr)

def othersolution_max(arr):
    return max(arr)


_min = othersolution_min
_max = othersolution_max

print(_min([-52, 56, 30, 29, -54, 0, -110]) == -110)
print(_min([42, 54, 65, 87, 0]) == 0)
print(_min([1, 2, 3, 4, 5, 10]) == 1)
print(_min([-1, -2, -3, -4, -5, -10]) == -10)
print(_min([9]) == 9)

print(_max([-52, 56, 30, 29, -54, 0, -110]) == 56)
print(_max([4, 6, 2, 1, 9, 63, -134, 566]) == 566)
print(_max([5]) == 5)
print(_max([534, 43, 2, 1, 3, 4, 5, 5, 443, 443, 555, 555]) == 555)
print(_max([9]) == 9)
