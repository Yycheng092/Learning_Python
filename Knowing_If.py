"""
if ──► elif ──► else 

if 中的比較運算子
相等          ==
不相等        != 
小於          <
小於或等於    <=  
大於          >
大於或等於    >=

false 值不一定是明確的布林 False ，以下都可以被視為 Fales 
布林        False
null        None
整數零        0
浮點數零     0.0 
空字串     '' or ""
空串列      []  
空 tuple    ()
空字典      {}
空集合      set()
"""

"""
因此我們可以透過這些特性來定義或檢查資料結構:
>>> some_list = []    # some_list 為一個空串列
>>> if some_list :    # 第一個先判斷 some_list 是否為 ture，但 some_list 指向的地方是一個空串列，所以為 False
>>>   print("There's something in here")
>>> else:
>>>   print("Hey, it's empty!")
# 最終結果為 Hey, it's empty!
"""

"""
if 的應用可以很多元
假如我想要判斷一個字母是不是母音，最一般的做法是寫一段很長的 if 陳述式 :
>>> letter ='o'
>>> if letter == 'a' or letter == 'ｅ' or letter == 'ｉ' or letter == 'ｏ' or letter == 'ｕ' :     # 利用 or 的特性，只要有一個為 true 結果即為 true
但有另外一種作法是改用成員運算子 in 
先將母音包裹在一個容器當中並指派給一個變數名稱  
>>> vowels = 'aeiou'
接著使用 in 運算子
>>> if letter in vowels :
if 會透過 letter 這個變數，進入容器，什麼容器呢，變數名稱為 vowels 的字串容器，由於字串是「可迭代物件（iterable）」所以可以被逐一遍歷，但凡有一個為 true 則結果即為 true 
"""










