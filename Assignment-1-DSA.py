#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Code-1  Write a program to find all pairs of an integer array whose sum is equal to a given number?

def getPairsCount(arr, n, sum):
 
    count = 0  
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
 
    return count
arr = [1, 5, 7, -1]
n = len(arr)
sum = 6
print("Count of pairs is",getPairsCount(arr, n, sum))


# In[3]:


# Code-2 Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)


# In[5]:


# Code-3 Write a program to check if two strings are a rotation of each other?

def checkRotation(s1, s2): 
    temp = '' 
    if len(s1) != len(s2): 
        return False
    temp = s1 + s1 
    if s2 in temp: 
        return True 
    else: 
        return False
string1 = "HELLO"
string2 = "LOHEL"
  
if checkRotation(string1, string2): 
    print("Given Strings are rotations of each other.")
else: 
    print("Given Strings are not rotations of each other.")


# In[12]:


# Code-4 Write a program to print the first non-repeated character from a string?

string = "Algorithm"
index = -1
temp = ""
 
if len(string) == 0 :
    print("EMTPY STRING");
for i in string:
    if string.count(i) == 1:
            temp += i
            break
    else:
            index += 1
if index == len(string)-1 :
    print("All characters are repeating ")
else:
    print("First non-repeating character is", temp)


# In[13]:


# Code-5 Read about the Tower of Hanoi algorithm. Write a program to implement it.

def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
N = 3
TowerOfHanoi(N, 'A', 'C', 'B')


# In[14]:


# Code -6 Write a program to convert postfix to prefix expression.

def isOperator(x):
 
    if x == "+":
        return True
 
    if x == "-":
        return True
 
    if x == "/":
        return True
 
    if x == "*":
        return True
 
    return False
 
def postToPre(post_exp):
 
    s = []
    length = len(post_exp)
    for i in range(length):

        if (isOperator(post_exp[i])):
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
            temp = post_exp[i] + op2 + op1
            s.append(temp)
        else:
            s.append(post_exp[i])
    ans = ""
    for i in s:
        ans += i
    return ans
if __name__ == "__main__":
 
    post_exp = "AB+CD-"
    print("Prefix : ", postToPre(post_exp))


# In[15]:


# Code-7 Write a program to convert prefix expression to infix expression.

def prefixToInfix(prefix):
    stack = []
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
            stack.append(prefix[i])
            i -= 1
        else:
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
    return stack.pop()
 
def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
if __name__=="__main__":
    str = "*-A/BC-/AKL"
    print(prefixToInfix(str))


# In[17]:


# Code-8 Write a program to check if all the brackets are closed in a given code snippet.

def BracketsBalanced(expr):
    stack = []
    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
    if stack:
        return False
    return True
if __name__ == "__main__":
    expr = "{()}[]"
    if BracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")


# In[19]:


# Code-9 Write a program to reverse a stack.

class Stack:
    def __init__(self):
        self.Elements = []
        
    def push(self, value):
        self.Elements.append(value)
       
    def pop(self):
        return self.Elements.pop()
    
    def empty(self):
        return self.Elements == []
    
    def show(self):
        for value in reversed(self.Elements):
            print(value)
            
def BottomInsert(s, value):

    if s.empty():
        s.push(value)
    else:
        popped = s.pop()
        BottomInsert(s, value)
        s.push(popped)

def Reverse(s):
    if s.empty():
        pass
    else:
        popped = s.pop()
        Reverse(s)
        BottomInsert(s, popped)
stk = Stack()
 
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)
 
print("Original Stack")
stk.show()
 
print("\nStack after Reversing")
Reverse(stk)
stk.show()


# In[21]:


# Code-10 Write a program to find the smallest number using a stack.

class MinStack(object):
    min=float('inf')
    def __init__(self):
        self.min=float('inf')
        self.stack = []
    def push(self, x):
        if x<=self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)
    def pop(self):
        t = self.stack[-1]
        self.stack.pop()
        if self.min == t:
            self.min = self.stack[-1]
            self.stack.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.min
m = MinStack()
m.push(-2)
m.push(0)
m.push(-3)
print(m.getMin())
m.pop()
print(m.top())
print(m.getMin())


# In[ ]:




