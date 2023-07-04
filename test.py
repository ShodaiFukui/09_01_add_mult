def min(a, b):
    if(a >= 0 and b >= 0 and a < b):
        return a
    if(a >= 0 and b >= 0 and a > b):
        return b
    if(a <= 0 and b <= 0 and a < b):
        return a
    if(a <= 0 and b <= 0 and a > b):
        return b
    if(a*b < 0):
        if(a < 0):
            return a
        if(b < 0):
            return b
    if(a == b):
        return a

    return 0

def main():
    return 0

if __name__ == "__main__":
    main()