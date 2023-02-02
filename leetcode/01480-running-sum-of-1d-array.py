class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        inserter = []
        summer = []
        for i in nums:
            inserter.append(i)
            suminsert = sum(inserter)
            summer.append(suminsert)
        return summer
