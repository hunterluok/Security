class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        c = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        sets = {k: v for k, v in zip(range(97, 123), c)}

        tempstr = set()

        for word in words:
            temp = []
            for w in word:
                temp.append(sets[ord(w)])
            tempstr.add(''.join(temp))
        return len(tempstr)

