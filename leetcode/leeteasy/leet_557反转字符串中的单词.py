class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) < 1:
            return s
        splits = s.split(" ")
        temp = []
        for strs in splits:
            temp_str = [i for i in strs]
            temp_str = temp_str[::-1]
            temp.append("".join(temp_str))
        return " ".join(temp)