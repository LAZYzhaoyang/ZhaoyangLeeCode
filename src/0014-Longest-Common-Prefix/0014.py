class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        loop = True
        add = True
        i = 0
        while loop:
            if i <len(strs[0]):
                pfix = strs[0][i]
            else:
                 break
            for j in range(len(strs)):
                if i <len(strs[j]):
                    f = strs[j][i] 
                else:
                    f = ''
                if f!=pfix:
                    loop=False
                    add=False
                    break
            if add:
                prefix = prefix+pfix
            i+=1
        return prefix    
