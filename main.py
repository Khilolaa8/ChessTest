def piyoda_check(x1, y1, x2, y2):
    return x1 == x2 and y2 - y1 == 1

def ruh_check(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2

def fil_check(x1, y1, x2, y2):
    return abs(x1 - x2) == abs(y1 - y2)

def ot_check(x1, y1, x2, y2):
    return (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2)

def farzin_check(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

def shoh_check(x1, y1, x2, y2):
    return max(abs(x1 - x2), abs(y1 - y2)) == 1

print(piyoda_check(2, 3, 2, 4))
print(ruh_check(1, 1, 1, 8))
print(fil_check(5, 5, 3, 3))
print(ot_check(4, 4, 6, 5))
print(farzin_check( 1,1, 1, 1))
print(shoh_check(4, 4, 5, 5))