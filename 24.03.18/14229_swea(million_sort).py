def msort(arr) :
    if len(arr) == 1 :
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = msort(left)
    right = msort(right)

    return merge(left, right)


def merge(left, right) :
    i = j = 0
    result = [0] * (len(left) + len(right))

    while i < len(left) and j < len(right) :        # 비교할 원소가 남아있을 경우 // 0부터 하나씩 올라가니까
        if left[i] > right[j] :     # left가 더 클 때,
            result[i+j] = right[j]
            j += 1

        else :   # right가 더 클 때,
            result[i+j] = left[i]
            i += 1

    # 둘 중 비교할 원소가 남아있지 않는게 있으면 반복문이 끝난다. 따라서 다른 쪽에 남아있는걸 추가해 줘야 함!
    while i < len(left) :
        result[i+j] = left[i]
        i += 1

    while j < len(right) :
        result[i+j] = right[j]
        j += 1

    return result




A = list(map(int, input().split()))

A = msort(A)
print(A[500000])