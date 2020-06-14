class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            j=len(digits)-1-i
            if(digits[j]==9):
                digits[j] = 0
                if digits[0] is 0:
                    digits.insert(0, 1)
            else:
                digits[j]+=1
                break
        return digits

