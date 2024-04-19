class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # new_arr = []
        # for i in arr:
        #     if i % 2 != 0:
        #         new_arr.append(i)
        #     if i % 2 != 1:
        #         new_arr
        arr_sorted = sorted(arr, key=lambda x: (bin(x).count('1'), x))
        return arr_sorted