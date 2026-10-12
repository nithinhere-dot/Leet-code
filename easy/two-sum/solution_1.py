class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length=len(nums)
        result=[]
        for i in range(length):
            first=nums[i]
            second=target-first
            for j in range(length-1):
                if(i==j):
                    continue
                else:
                    if(second==nums[j]):
                        result.append(j)
                        result.append(i)
                        return result
                        

        return result


        
