"""
在 Python 中 module 就是一個 .py 檔案
只要一個 Python 檔案，可以被其他程式 import，那它就是一個 module
但能被 import 的不一定是 module，也可能是 package
一個 package 一定存在一隻初始化的 .py，__init__.py 這隻檔案

在模組中裡面通常可以放  1.variable 2.function 3.class(物件) 

file : math_tools.py    # math_tools.py 即為一個模組
PI = 3.14159    # 1.variable

def add(a,b):    # 2.function
  return a + b 

class Calculator :    #3. class 
  def multiply(self , a , b):
    return a * b 

所以在 math_tools.py 的結構中是這樣
math_tools (module)
 ├─ PI (variable)
 ├─ add (function)
 └─ Calculator (class)

那如何使用呢?
如果有另一個程式 import math_tools
那麼他就可以使用裡面的內容，像是
math_tools.PI
math_tools.add(2,3)
math_tools.Calculator()
"""
