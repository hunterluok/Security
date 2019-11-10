class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        new = []
        temp = []
        flag = 0
        for i in S:
            if i == "(":
                flag += 1
                temp.append(i)
            else:
                flag -= 1
                temp.append(i)
            if flag == 0:
                new.extend(temp[1:-1])
                temp = []
        return "".join(new)