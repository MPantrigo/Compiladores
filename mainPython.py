def main(): 
    a = input()
    a = float(a)
    b = input()
    b = float(b)
    c = 10

    a = 1+2*3/b

    t1 = "Enquanto"

    t2 = t1

    if c>b:
        print(a)
        if c>b:
            print(b)

    while b<c:
        a = a+1
        while b<c:
            b = b+1

    match a:
        case 10:
            print(a)
        case 20:
            print(a)
        case default :
            print(a)

