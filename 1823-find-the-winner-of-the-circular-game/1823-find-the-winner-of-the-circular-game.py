class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = []
        index = 0
        for i in range(1, n+1):
            arr.append(i)
            # arr = [i for i in range(1, n+1)]
        while len(arr) > 1:
            index = (index + k - 1) % len(arr)
            arr.pop(index)
        return arr[0]