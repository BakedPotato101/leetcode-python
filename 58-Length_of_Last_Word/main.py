class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sentence = s.split()
        last = len(sentence) - 1
        if len(sentence) == 1:
            return len(sentence[0])
        else:
            return len(sentence[last])