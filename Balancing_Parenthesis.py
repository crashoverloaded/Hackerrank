#!/usr/bin/python3

class Stack():
	def __init__(self):
		self.items=[]
	def push(self,item):
		self.items.append(item)
	def is_empty(self):
		return self.items == []
	def pop(self):
		return self.items.pop()
	def get_stack(self):
                return self.items

def is_match(p1,p2):
	if p1=="{" and p2=="}":
		return True
	if p1=="<" and p2==">":
		return True
	if p1=="[" and p2=="]":
		return True
	if p1=="(" and p2==")":
		return True
	else:
		return False
def balance_paren(input_string):
	s=Stack()
	is_balanced=True
	for i in input_string:
		if i in "{<([":
			s.push(i)
		else:
			if s.is_empty():
				break
			else:
				top = s.pop()
				if not is_match(top,i):
					is_balanced=False
					break
	if s.is_empty() and is_balanced == True:
		return True
	else:
		return False 
print(balance_paren(input("Enter Parenthesis String:-"))		)
