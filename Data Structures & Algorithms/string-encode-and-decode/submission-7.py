class Solution:

    # for each string, compute length and add "length#string"
    def encode(self, strs: List[str]) -> str:
        total_string = ""
        for s in strs:
            total_string += str(len(s))
            total_string += "#"
            total_string += s
        return total_string

    # initalize empty list for decoded string and pointer i = 0
    # move j until # to find length, move i and extract # characters
    # move i by length to continue decoding next segment
    def decode(self, s: str) -> List[str]:
        strs = []
        
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i : j])
            i = j + 1
            j = i + length
            strs.append(s[i : j])
            i = j
        return strs
