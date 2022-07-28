class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
            num = []
            l = m = n
            for i in range(1,len(nums)+1):
                if i%2!=0:
                    num.append(nums[l-n])
                    l=l+1
                else:
                    num.append(nums[m])
                    m+=1
            return num