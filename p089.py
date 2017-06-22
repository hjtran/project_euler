ones_dict = ['',
            'I',
            'II',
            'III',
            'IV',
            'V',
            'VI',
            'VII',
            'VIII',
            'IX']
tens_dict = ['',
            'X',
            'XX',
            'XXX',
            'XL',
            'L',
            'LX',
            'LXX',
            'LXXX',
            'XC']
hunds_dict = ['',
            'C',
            'CC',
            'CCC',
            'CD',
            'D',
            'DC',
            'DCC',
            'DCCC',
            'CM']
thous_dict = ['',
        'M',
        'MM',
        'MMM',
        'MMMM',
        'MMMMM']
def roman_writer(num):

    ones = num % 10
    tens = num % 100 // 10
    hunds = num % 1000 // 100
    thous = num % 10000 // 1000


    s = []

    if thous > 0:
        s.append(thous_dict[thous])
    if hunds > 0:
        s.append(hunds_dict[hunds])
    if tens > 0:
        s.append(tens_dict[tens])
    if ones > 0:
        s.append(ones_dict[ones])

    return ''.join(s)

def roman_reader(num):
    table = {'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000}

    s = 0
    idx = 0
    while idx < len(num):
        if idx != len(num)-1 and table[num[idx]] < table[num[idx+1]]:
            s += table[num[idx+1]]-table[num[idx]]
            idx += 2
        else:
            s += table[num[idx]]
            idx += 1

    return s


with open('inputs/p089.txt','r') as infile:
    savings = 0
    for line in infile:
        r = line.strip()
        min_r = roman_writer(roman_reader(r))
        savings += len(r)-len(min_r)
print(savings)

