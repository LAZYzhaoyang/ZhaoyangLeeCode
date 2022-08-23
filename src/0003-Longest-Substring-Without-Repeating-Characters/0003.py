class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen=0
        l = len(s)
        pre=0
        while pre<l:
            sub = [s[pre]]
            j=pre+1
            while j<l:
                new_s = s[j]
                if new_s not in sub:
                    sub.append(new_s)
                    j+=1
                else:
                    break
            new_l = len(sub)
            if new_l>maxlen:
                maxlen=new_l
            pre+=1
        return maxlen
