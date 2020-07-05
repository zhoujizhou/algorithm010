class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten=0
        for i in bills:
            if i == 5:
                five+=1
            elif i == 10:
                if five == 0:
                    return False
                five-=1
                ten+=1
            else:
                if five ==0 :
                    return False
                elif ten == 0 :
                    if five > 2:
                        five -= 3
                    else:
                        return False
                else:
                    five-=1
                    ten-=1
        return True
