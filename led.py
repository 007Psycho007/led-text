def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]

a = [1,2,3,4]
b = shift(a,1)
print(b)
