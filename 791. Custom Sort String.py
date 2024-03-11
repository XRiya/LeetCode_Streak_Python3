class Solution:
    def customSortString(self, order: str, s: str) -> str:
        not_order = "".join([i for i in s if i not in order])
        count = Counter(s)
        res = ""
        for i in order:
            if i in s:
                res+=i*count[i]
        return res+not_order
