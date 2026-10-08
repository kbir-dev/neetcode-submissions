class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {")":"(", "}":"{","]":"["}
        stk=[]
        for c in s:
            if c not in mapp:
                stk.append(c)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != mapp[c]:
                        return False
        return not stk