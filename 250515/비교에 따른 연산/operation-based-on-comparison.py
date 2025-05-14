nums = input()

a,b = map(int, nums.split())

if a > b:
    print(a*b)
else:
    print(b//a)