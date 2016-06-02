
for n in range(10,100):
    for d in range(n+1,100):
        digs = set(list(str(n)+str(d)))
        try:
            cancels = [(int(str(n).strip(dig)),int(str(d).strip(dig))) for dig in digs]
            for c in cancels:
                if c[0]/float(c[1]) == n/float(d):
                    print n,d
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
