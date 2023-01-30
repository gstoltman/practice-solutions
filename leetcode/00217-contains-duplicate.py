class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mylist = []
        for i in nums:
            if i in mylist:
                return True
            mylist.append(i)
        return False
