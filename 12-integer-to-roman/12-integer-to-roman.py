class Solution:
    def intToRoman(self, num: int) -> str:
        '''
        The logic here is if the previous value is smaller than the current value
        we subtract from the final result, other wise we add. 
        
        IV = 5-1 = 4
        VI = 5+1 = 6
        
        '''
        
        ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hundreds = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        thos = ["","M","MM","MMM"]
        
        return thos[num//1000] + hundreds[num%1000//100] + tens[num%100//10] + ones[num%10]
        