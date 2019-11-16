class Solution:
    def judgeCircle(self, moves: str) -> bool:
        left_count = 0
        up_count = 0
        for ele in moves:
            if ele == 'R':
                left_count -= 1
            elif ele == 'L':
                left_count += 1
            elif ele == 'U':
                up_count += 1
            else:
                up_count -= 1
        if left_count == 0 and up_count == 0:
            return True
        else:
            return False