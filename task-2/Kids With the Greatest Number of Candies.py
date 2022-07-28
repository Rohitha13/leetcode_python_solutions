class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        num = max(candies)
        res = []
        for i in candies:
                res.append(i + extraCandies >=num)

        return res