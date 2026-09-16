class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        res = []

        for items in Counter(nums).most_common(k):
            res.append(items[0])
        return res