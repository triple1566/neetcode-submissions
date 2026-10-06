class Solution:
    def isValid(self, s: str) -> bool:
        # Constraints:
        # 1 <= s.length <= 1000
        stack=[]
        for c in s:
            if c=='(':
                stack.append(')')
                continue
            elif c=='{':
                stack.append('}')
                continue
            elif c=='[':
                stack.append(']')
                continue
            elif c==')':
                if not len(stack):
                    return False
                if c==stack.pop():
                    continue
                else:
                    return False
            elif c=='}':
                if not len(stack):
                    return False
                if c==stack.pop():
                    continue
                else:
                    return False
            elif c==']':
                if not len(stack):
                    return False
                if c==stack.pop():
                    continue
                else:
                    return False
        
        if len(stack):
            return False
        return True
                