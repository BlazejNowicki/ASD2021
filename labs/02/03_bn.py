def mergesort(T):
    l=len(T)
    if l==1:return T,0
    A,x = mergesort(T[:l//2])
    B,y = mergesort(T[l//2:])
    inv_counter=x+y
    i=j=k=0
    while i<len(A) or j<len(B):
        if j>=len(B) or ( i<len(A) and A[i] <= B[j] ):
            T[k]=A[i]
            i += 1
        else:
            T[k]=B[j]
            j += 1
            inv_counter += len(A)-i
        k += 1
    return T, inv_counter

def inversions(T):
    _, ans = mergesort(T)
    return ans

if __name__ == "__main__":
    # not sure it always works
    T=[10,22,3,4,5,6,8,16]
    print(T)
    print(inversions(T))
