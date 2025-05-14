nums = input()
a,b = map(int, nums.split())

for i in range(b, a-1, -1):
    print(i, end=" ")
