for countdown in 5,4,3,2,1,"hey!":
    print(countdown)

for 變數 in 容器(tuple or list)
    print()
  
"""
5,4,3,2,1,"hey!" 其實是一個 tuple 或 list
在 python 中允許將 (5,4,3,2,1,"hey!") 或 [5,4,3,2,1,"hey!"] 的內容寫成這樣 5,4,3,2,1,"hey!"
而不管是哪一種寫法我們都可以將它理解為這個容器當中裝著 int5、int4、int3、int2、int1、str"hey!"
因為 Python 是動態型別 (Dynamic Typing) 所以程式會自動判斷容器當中是整數還是字串還是其他型別等
可以透過這行來觀察 print(countdown, type(countdown))
"""

-
for countdown in 5,4,3,2,1,"hey!":
    print(countdown)
所以當程式運行時會做什麼事?
python 的理解會是
1.看到一個「可迭代物件」(tuple)
2.從第一個元素開始
3.拿出來
4.放進 countdown
5.列印
6.再拿下一個
7.重複直到拿完
---

-
那 python 怎麼知道要往下一個搜尋直到結束?
因為在 python 內部有一個叫做 iterator 迭代器的機制
當我寫出 for x in 容器: 時
Python 會在背後偷偷做這件事
1.建立一個 iterator
2.一直問它：還有沒有下一個？
3.如果有 → 拿出來
4.如果沒有 → 結束
---

-
結果會印出什麼?
5
4
3
2
1
hey!
---

















  
