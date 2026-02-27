"""
在Python 中

作業系統允許 python 程式存取電腦的一些記憶體，讓其用那些記憶體存取程式碼本身，
程式會自動追蹤他們的位元在哪裡(也就是在記憶體中的哪一個位置)，以及他們是什麼資料型態，
對於電腦來說，他們所占用的皆是位元，但同一組位元可能代表著不同的東西，取決於我們指定他是什麼東西，
65 可以代表著數字，也可以代表著文字位元 A，
一般來說，我們所使用的電腦是 64 位元，這意味著一個 int 所占用的是 64 bits，也就是 8 Bytes，
"""

"""
型態
Python 基本常見的型態
        "型態"              是否可改變       範例
bool                           否           True, False
int                            否           47, 50000 25_000
float                          否           3.14, 2.7e5
complex (複數)                 否           3j, 5 + 9j
str                            否           'alas', "alack", '''a verse attack'''
list (串列)                    是           ['Winken', 'Nod','Dlinken']
tuple                          否           (2,4,8)
bytes                          否           b'ab\xff
bytearray                      是           bytearray(...)
set (集合)                     是           set([3,5,7])
frozenset (不可變集合)          否          forzenset(['Elsa', 'Otto'])
dict (字典)                    是           {'game':'bingo' , 'dog':'dingo' , 'drummer':'Ringo'}
這邊的可變與不可變是指，由於 python 是強定型(strongly typed)的，意思是改的是「物件本身」，不是改「變數名稱」
-可變（mutable）＝物件內容可以直接被改
-不可變（immutable）＝物件內容不能被改，只能產生新物件
"""

"""
賦值
在 python 中我們可以用 = 將一個值指派給一個變數，也就是將右邊的值指派給左邊的變數
"""

"""
變數
"變數 = 物件"
在 python 中「變數僅代表名稱」不代表位置，這點與其他多個電腦語言不同
在 python 中若想要了解一個變數的型態，可以使用 print(type(...))
在 python 中可以將一個值指派給多個變數名稱
"""

"""
型態可變與不可變的重要性
a = [1, 2, 3]，發生的事情其實是：a ───►  [1, 2, 3]，a 只是「指向」那個物件。
👉同一個物件被修改，沒有產生新物件這叫「可變」
s = "hello"，s = s + " world"，發生的事情是：
第一步：s ───►  "hello"
第二步：建立新物件 "hello world"，s ───►  "hello world"
此時沒有任何變數再指向 "hello"，所以它的 reference count 會變成 0，所以Python 會回收它
"""
























