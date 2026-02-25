#6. Zig Zag Conversion
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        ls=[[] for i in range(numRows)]
        ofset=2*numRows-2
        print(ofset)
        for i in range(0,len(s)):
            if i%(ofset) < numRows:
                ls[i%(ofset)].extend(s[i])
            else:
                ls[-(i%(ofset))+(ofset)].extend(s[i])
        op=''.join([''.join(i) for i in ls])
        return op