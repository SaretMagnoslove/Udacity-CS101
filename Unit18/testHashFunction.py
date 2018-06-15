def textHashFunction(func, keys, size):
    result = [0] * size
    keysUsed = []
    for key in keys:
        if key not in keysUsed:
            hv = func(key, size)
            result[hv] += 1
            keysUsed.append(key)
    return result
    