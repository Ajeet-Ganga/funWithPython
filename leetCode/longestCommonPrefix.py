class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        slen = [len(l) for l in strs]
        if min(slen) == 0:
            return ""
        for i in range(1,min(slen)+1):#1
            for s in strs:#a
                if not s.startswith(strs[0][:i]):#a a
                    if (i == 1):
                        return ""
                    else:
                        return strs[0][:i-1]
            if i == min(slen):
                return strs[0][:i]
    