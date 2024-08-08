class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        # score.sort(key=lambda x: x[k], reverse=True)
        # return score
        nums = []
        for i in range(len(score)):
            for j in range(len(score[i])):
                if j == k:
                    nums.append(score[i][j])

        for a in range(len(nums)-1):
            for b in range(a + 1, len(nums)):
                if nums[a] < nums[b]:
                    nums[a], nums[b] = nums[b], nums[a]
                    score[a], score[b] = score[b], score[a]
        return score