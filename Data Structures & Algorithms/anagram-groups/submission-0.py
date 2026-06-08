class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # HASH MAP
        mapping = defaultdict(list)     # map charCount to list of anagram

        for s in strs:
            count = [0] * 26            # a ... z
            for char in s:
                # a = 80 | 80 - 80 = 0
                # b = 81 | 81 - 80 = 0
                count[ord(char) - ord('a')] += 1
            # list -> tuple bc list cannot be keys
            mapping[tuple(count)].append(s)
        return list(mapping.values())

        # SORTING
        mapping = defaultdict(list)
        for s in strs:
            sorted_arr = ''.join(sorted(s))
            mapping[sorted_arr].append(s)
        return list(mapping.values())
        