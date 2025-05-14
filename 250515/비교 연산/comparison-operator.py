nums = input()

A,B = map(int, nums.split())

if A >= B:
    print(1)
else:
    print(0)
if A > B:
    print(1)
else:
    print(0)
if B >= A:
    print(1)
else:
    print(0)
if B > A:
    print(1)
else:
    print(0)
if A == B:
    print(1)
else:
    print(0)
if A != B:
    print(1)
else:
    print(0)