class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""
        for s in strs:
            final_str += str(len(s)) + "#" + s
        return final_str

    def decode(self, s: str) -> List[str]:
        final_list = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i : j])
            i = j + 1
            
            final_list.append(s[i : i + length])
            i += length
        return final_list

        # return s.split(" ")
