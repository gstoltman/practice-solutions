class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        tuples = []
        dict = {}
        for i in strs:
            tuples.append((''.join(sorted(i)), i))
        for key, value in tuples:
            if key in dict:
                dict[key].append(value)
            else:
                dict[key] = [value]
        for i in dict.values():
            answer.append(i)
        return answer
