def valid (v):
    if v % 7 == 0 and v % 11 == 0 and v % 13 == 0 and v % 14 == 0 and v % 15 == 0 and v % 16 == 0 and v % 17 == 0 and v % 18 == 0 and v % 19 == 0 and v % 20 == 0 :
        return True
    else: 
        return False

if __name__ == "__main__":
    val = 100000000
    while True:
        if valid(val) or val > 1000000000:
            print(val)
            break
        else:
            # we need to increment by the largest number needed to be divisible evenly
            val = 20 + val
