def partition(A, lo, hi):
    pivot = A[lo + (hi - lo) // 2]
    i = lo - 1
    j = hi + 1

    while True:
        
        i += 1
        while A[i] < pivot:
            i += 1
        
        j -= 1    
        while A[j] > pivot:
            j -= 1
            
        if i >= j:
            return j
        A[i], A[j] = A[j], A[i]

def quicksort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p)
        quicksort(A, p + 1, hi)
    return A

if __name__ == "__main__":
    arr = [8, 3, 5, 1, 7, 2]
    quicksort(arr, 0, len(arr) - 1)
    # >>> [1, 2, 3, 5, 7, 8]
