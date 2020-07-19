class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        #set
        if n<=0: return []
        res = []
        def dfs(row, cols, pie, na, cur_state):
            #terminator
            if row >= n:
                res.append(cur_state)
                return
            for col in range(n):
                if col not in cols and (row+col) not in pie and (row-col) not in  na:
                    dfs(row+1, {col}|cols, {row+col}|pie, {row-col}|na, cur_state+[col])
        dfs(0, set(), set(), set(), [])
        return [['.'*i+'Q'+(n-i-1)*'.' for i in col] for col in res]
        '''
        if n<=0: return []
        res = []
        def dfs(row, cols, pie, na, cur_state):
            if row >= n: 
                res.append(cur_state)
                return
            bits = (~(cols|pie|na))&((1<<n)-1)
            while bits>0:
                P = bits&(-bits)  #取出最低位的1
                mask, count =1, 0
                while mask&P == 0:  #得出其位数，如果不加mask是1248
                    count +=1
                    mask = mask<<1
                bits = bits&(bits-1)
                dfs(row+1, P|cols, (P|pie)<<1, (P|na)>>1, cur_state+[count])

        dfs(0, 0, 0, 0, [])
        return [['.'*i+'Q'+(n-i-1)*'.' for i in col] for col in res]