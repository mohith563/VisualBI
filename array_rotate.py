n, k = map(int, input().split())
arr = [i for i in input().split(',')]


def index_based(arr, n, k):
    shifted = arr[:]
    for i in range(n):
        pos = (i + k) % n
        shifted[pos] = arr[i]
    return shifted


def slice_based(arr, n, k):
    return arr[k % n:]+arr[:k % n]


print(index_based(arr, n, k))
print(slice_based(arr, n, -k))
