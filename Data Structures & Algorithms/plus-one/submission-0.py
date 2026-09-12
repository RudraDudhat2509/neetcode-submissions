class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''.join(str(d) for d in digits)
        i = int(string)
        i += 1
        string = str(i)
        return [int(x) for x in string]