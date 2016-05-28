

ones = {
        0:'',
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine',
        10:'ten',
        11:'eleven',
        12:'twelve',
        13:'thirteen',
        14:'fourteen',
        15:'fifteen',
        16:'sixteen',
        17:'seventeen',
        18:'eighteen',
        19:'nineteen',
        }
tens = {
            0:'',
            2:'twenty',
            3:'thirty',
            4:'forty',
            5:'fifty',
            6:'sixty',
            7:'seventy',
            8:'eighty',
            9:'ninety',
            }

s = 0
for i in range(1,1001):
    if i < 20:
        s += len(ones[i])
        print ones[i]
    elif i < 100:
        s+= len(tens[i/10])
        s+= len(ones[i%10])
        print tens[i/10]+ones[i%10]
    elif i < 1000:
        s+= len(ones[i/100])
        s+= len('hundredand')
        if (i/10)%10 > 1:
            s+= len(tens[(i/10)%10])
            s+= len(ones[i%10])
            print ones[i/100] + ' and ' + tens[(i/10)%10] + ones[i%10]
        else:
            s+= len(ones[i%100])
            print ones[i/100] + ' and ' + ones[i%100]
            

    else:
        s+= len('onethousand')
print s
