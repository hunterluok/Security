class Solution:
    def flipAndInvertImage(self, A):
        news = []
        for line in A:
            line = line[::-1]
            line = [1-i for i in line]
            news.append(line)
        return news