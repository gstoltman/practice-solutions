class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mylist = []
        for n in nums:
            if n in mylist:
                return True
            mylist.append(n)
        return False
