class Solution:
    def isHappy(self, n: int) -> bool:
        sum = 0
        if n == 1 or n == 7:
            return True
        elif n < 10:
            return False
        else:
            while n > 0:
                temp = n%10
                sum += temp*temp
                n = n//10
            return self.isHappy(sum)

            