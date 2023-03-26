class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        add = 0;
        for i in accounts:
            add = sum(i)
            max_wealth = max(max_wealth, add)
        return max_wealth