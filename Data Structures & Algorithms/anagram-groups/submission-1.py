class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # BRUTE FORCE
        # alphabeticalize every string


        # HASH MAP
        stringMap = defaultdict(list)
        for i, s in enumerate(strs):
            stringMap[tuple(sorted(s))].append(s)
        
        return list(stringMap.values())
        