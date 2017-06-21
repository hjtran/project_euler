from fractions import Fraction

        
seq = [2]
for k in range(1,34):
    seq.extend([1,2*k,1])


def find_nth_conv(n,seq,idx):
    if idx == n-1:
        return Fraction(1,seq[idx])
    else:
        return Fraction(1,seq[idx]+find_nth_conv(n,seq,idx+1))

f = Fraction(seq[0],1)+find_nth_conv(100,seq,1)

s = sum([int(d) for d in str(f.numerator)])
print(s)
