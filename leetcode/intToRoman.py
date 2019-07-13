class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ''
        roman = roman + (num//1000)*'M'
        if num%1000 >= 400 and num%1000 < 500:
        	roman = roman + 'CD'
        elif num%1000 >= 900:
        	roman = roman + 'CM'
        else:
        	roman = roman + (num%1000//500)*'D'
        	roman = roman + (num%1000%500//100)*'C'
        if num%1000%500%100 >= 40 and num%1000%500%100 < 50:
        	roman = roman + 'XL'
        elif num%1000%500%100 >= 90:
        	roman = roman + 'XC'
        else:
        	roman = roman + (num%1000%500%100//50)*'L'
        	roman = roman + (num%1000%500%100%50//10)*'X'
        if num%1000%500%100%50%10 == 4:
        	roman = roman + 'IV'
        elif num%1000%500%100%50%10 == 9:
        	roman = roman + 'IX'
        else:
        	roman = roman + (num%1000%500%100%50%10//5)*'V'
        	roman = roman + (num%1000%500%100%50%10%5)*'I'
        return roman

# class Solution:
#     def intToRoman(self, num):
#         """
#         :type num: int
#         :rtype: str
#         """
# 		M = ["", "M", "MM", "MMM"];
# 		C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
# 		X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
# 		I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
# 		return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10];

s = 1994
t = Solution()
a=t.intToRoman(s)
print(a)






        