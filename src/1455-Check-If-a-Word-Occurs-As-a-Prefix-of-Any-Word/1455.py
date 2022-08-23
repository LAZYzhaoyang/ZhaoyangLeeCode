class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        senlist = list(split(sentence, ' '))
        out=-1
        num = len(searchWord)
        for i in range(len(senlist)):
            if len(senlist[i])>=num:
                pre = senlist[i][:num]
                if pre == searchWord:
                    out=i+1
                    break
        return out
