class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        self.res = []
        self.helper(n, k, index = 1, cur_state= [])
        return self.res
    def helper(self, n, k, index, cur_state):
        if len(cur_state)==k:
            self.res.append(cur_state)
            return
        for i in range(index, n+1):
            self.helper(n,k, i+1, cur_state+[i])
        '''
        self.res = []
        self.helper(n, k, index = 1, cur_state= [])
        return self.res
    def helper(self, n, k, index, cur_state):
        if len(cur_state)==k:
            self.res.append(cur_state[:])
            return
        for i in range(index, n+1):
            cur_state.append(i)
            self.helper(n,k, i+1, cur_state)
            cur_state.pop()