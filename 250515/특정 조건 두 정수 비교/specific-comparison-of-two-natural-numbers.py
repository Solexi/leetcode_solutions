nums = input()

A,B = map(int, nums.split())

if A < B:
    print(1, 0, sep=" ")
elif A == B:
    print (0, 1, sep=" ")
else:
    print(0, 0, sep=" ")