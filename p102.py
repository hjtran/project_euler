
def find_y_intercept(pt1,pt2):
    x1,y1 = pt1
    x2,y2 = pt2
    if (x2-x1) == 0:
        return float('Inf')
    else:
        m = (y2-y1)/(x2-x1)
        return y1-m*x1

def within_interval(pt1,pt2):
    maxy = max(pt1[1],pt2[1])
    miny = min(pt1[1],pt2[1])
    if find_y_intercept(pt1,pt2) == float('Inf'):
        return pt1[0] == 0 and pt2[1] == 0 and miny <= 0 and maxy >= 0
    else:
        y_int = find_y_intercept(pt1,pt2)
        return  y_int<= maxy and y_int >= miny and y_int >= 0

def contains(pt1,pt2,pt3):

    if pt1 == [0,0] or pt2 == [0,0] or pt3 == [0,0]:
        print('test')
        return True
    elif find_y_intercept(pt1,pt2) == 0 or find_y_intercept(pt2,pt3)==0 or find_y_intercept(pt3,pt1)==0:
        print('test')
        return True
    elif (within_interval(pt1,pt2) + within_interval(pt2,pt3) + within_interval(pt3,pt1)) == 1:
        return True
    else:
        return False

num_contain = 0
with open('inputs/p102.txt','r') as infile:
    for line in infile:
        coords = list(map(int,line.strip().split(',')))
        pt1 = coords[0:2]
        pt2 = coords[2:4]
        pt3 = coords[4:6]
        if contains(pt1,pt2,pt3):
            num_contain += 1

print(num_contain)



