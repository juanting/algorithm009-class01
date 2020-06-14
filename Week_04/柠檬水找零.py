class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if not bills: return True
        five, ten = 0, 0
        for coin in  bills:
            if coin == 5:
                five+=1
            elif coin == 10:
                five -=1
                ten +=1
            else:
                if ten>0:
                    five -=1
                    ten -=1
                else:
                    five -=3
            if five < 0 or ten < 0:
                return False
        return True