class Solution:
    def addDigits(self, num: int) -> int:
        
        def sum_digits(num):
            total=0
            while num>0:
                total = total + num%10
                num=num//10        
            return total
        
        while num>9:
            num=sum_digits(num)

        return num
