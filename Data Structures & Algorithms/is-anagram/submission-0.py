class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic={}
        for i in s:
            dic[i]= dic.get(i,0)+1
        for i in t:
            dic[i]=dic.get(i,0)-1
        for i in dic:
            if dic[i]!=0:
                return False
        return True