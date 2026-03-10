#10-03-2026
#71. Simplify Path
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        pathl = [p for p in path.split('/') if p]
        for i in pathl:
            if stack:
                if i=='.':
                    continue
                if i=='..':
                    stack.pop()
                    continue
            else:
                if i=='.' or i=='..':
                    continue
            stack.append(f'/{i}')
        return ''.join(stack) if stack else '/'