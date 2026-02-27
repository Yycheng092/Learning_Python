第一種
for x in "ABC":
  print(x)    # print("ABC"[0])   #A

第二種
for x in ["ABC"]:
  print(x)

第三種
for x in ("ABC"):
  print(x)

第四種
for x in ("ABC",):
  print(x)

"""
觀念釐清 for 是對 容器 做走訪，也就是 for 是對 iterable 走訪，那容器可以是 list / tuple / string，而list / tuple / string 也都是 iterable
在 python 中，不同於人類的直覺認為容器中有幾個元素，而是依照「型別本身是如何定義」
在 python 中，string / list / tuple 皆屬於「序列型別」，也就是可以當作 index 來存取
"""     

"""
回到第一種 
for x in "ABC":
  print(x)   
for 對 in 後面的容器做走訪，此時 in 後面的容器為 string，且沒有外層容器，而 string 是 iterable，可以當作 index 來存取，所以 string 本身會被拆開
總共拆開三次，所以結果會分別列印 A、B、C
"""

"""
若想將第二種的答案與第一種的答案相同該怎麼寫
for x in ["ABC"]:
    for y in x:
        print(y)
首先 for 對 容器，此時容器為 list，在 list 當中有幾個元素? 一個，所以只會跑一次，抓取第一個結果出來為 "ABC"，此時為 string 型別，這時 for 對應到的容器為 string 
，又因為 string 本身就是由字元組成的序列，所以 for 會依序取出 index 的每個字元，此時列印出的結果為 A、B、C
"""

"""
第三種與第四種的差別是什麼?
很多人會認為有括號就是 tuple，但其實判斷 tuple 的方式並非在於括號，而是有沒有逗號
print(type(("ABC")))   # <class 'str'>
print(type(("ABC",)))  # <class 'tuple'>
在 python 的理解當中，括號會被理解為分組用，並非 tuple
所以第三種的結果是 A、B、C
第四種的結果是 ABC
"""




