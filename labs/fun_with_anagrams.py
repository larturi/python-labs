def funWithAnagrams(arr):
    limit = len(arr)
    arr.reverse()
    arr_result = list(arr)

    count = 0
    for i in range(0, limit):
        if arr[i+1:] and isAnagram(arr[i], arr[i+1:]):
            arr_result.pop(i - count)
            count += 1

    return sorted(arr_result)


def isAnagram(word, arr):
    for x in arr:
        if (sorted(word) == sorted(x)):
            return True
    return False


str = ['code', 'doce', 'ecod', 'framer', 'frame']

print(funWithAnagrams(str))