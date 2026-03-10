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
    
'''
Improvements

In taking care of the EMPTY casees i realised we will end up with an empty stack in the end in either of the cases so instead of using multiple if statements for each it makes sense to 

`return ''.join(stack) if stack else '/'` 

This is a far smarter way of solving it.
### Final Code’s Space and Time complexity Analysis

1. Time complexity
    1. Creating the path list costs us $O(n)$ linear time
    2. Iterating through the list costs us another $O(n)$ linear time 
    3. Appending to the list is an amortized $O(1)$ constant time complexity
    4. The final return statements costs $O(n)$ linear time again

Since all our operations cost $O(n)$ our final Time Complexity is $O(n)$

1. Space Complexity
    1. Creating the path list costs us $O(n)$
    2. All the operations in the for loop are $O(1)$
    3. As we are creating a stack based on the original string its space complexity is a worst case of $O(n)$ 
    4. The final statements time complexity is also $O(n)$ 

As all our operations here cost $O(n)$ space too our final Space Complexity is $O(n)$
'''