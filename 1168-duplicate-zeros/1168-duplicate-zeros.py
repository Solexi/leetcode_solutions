class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if 0 not in arr:
            return arr
        i = 0
        while i < len(arr):
            if arr[i] != 0:
                i += 1
            else:
                arr.insert(i+1, 0)
                arr.pop()
                i += 2
        