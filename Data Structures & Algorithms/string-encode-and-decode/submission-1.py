class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        # ['the', 'fox', 'tale'] --> 3#the3#fox4#tale
        for s in strs:
            l = len(s)
            encoded_str += str(l)+"#"+s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            j = i
            # for finding length
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            # read the string based on length
            string = s[j+1 : j+1+length]
            # append it
            decoded_strs.append(string)
            # move i to next index of the current string end
            i = j + 1 + length
        return decoded_strs
            

