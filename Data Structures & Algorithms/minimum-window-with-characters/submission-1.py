class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        t_freq = Counter(t)
        s_freq = Counter()
        need = len(t_freq)
        have = 0

        start = 0
        end = 0
        bestl,bestr = 0, float("inf")


        while end < len(s):
            cur = s[end]
            s_freq[cur] += 1
            if cur in t_freq and s_freq[cur] == t_freq[cur]:
                have += 1

            while have == need:
                if end - start < bestr - bestl:
                    bestl,bestr = start,end
                
                delete = s[start]
                s_freq[delete] -= 1
                if delete in t_freq and s_freq[delete] < t_freq[delete]:
                    have -= 1
                
                



                start += 1
            end += 1



        if bestr != float("inf"):
            return s[bestl:bestr + 1]
        return ""
