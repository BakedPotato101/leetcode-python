class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        p1 = 0
        p2 = 0
        outputLength = len(word1) + len(word2)
        print(f"length of output: {outputLength}")
        for c in range(0, outputLength):
            print(f"cycle: {c}")
            try:
                output.append(word1[p1])
                print(f"appending: {word1[p1]}")
                p1 += 1
            except IndexError:
                print("Word1 has no more characters to append")
            finally:
                None

            try:
                output.append(word2[p2])
                print(f"appending: {word2[p2]}")
                p2 += 1
            except IndexError:
                print("Word2 has no more characters to append")
            finally:
                 None

        return "".join(output)
    
s = Solution()
print(s.mergeAlternately("a","ps"))

