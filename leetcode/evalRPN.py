class Solution:
	def evalRPN(self, tokens):
		stack = []
		for i in tokens:
			if i not in '+-*/':
				stack.append(i)
			else:
				a = stack.pop()
				b = stack.pop()
				res = int(eval(b+i+a))
				stack.append(str(res))
		return stack[-1]


        

        
s = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
t = Solution()
print(t.evalRPN(s))