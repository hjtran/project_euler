

x = 1
while True:
    print x
    str_x = sorted(str(x))
    if all([True if sorted(str(x*i))==str_x else False for i in range(2,7) ]):
        break
    x += 1

print
print x


