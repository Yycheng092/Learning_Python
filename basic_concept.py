"""
Series 是 1D  
DataFrame 是 2D，可以理解為需要同時擁有 行 * 列 的表格才能找到對應的值
"""

"""
class、instance、string、int、list、dict、function、DataFrame，這些全部都可以稱為物件，但變數不是

DataFrame 物件是「二維的資料結構」內部有很多屬性
│
├── index
├── columns
├── dtypes 
├── values
└── methods (head, mean, etc.)
"""

-
str 與 list 的差別

型別上的差異
len("date")      # 4  # str
len(["date"])    # 1  # list

結構上的差異
編碼 "date"，等於 'd' 'a' 't' 'e' 他是四個元素，每一個元素都是一個字元
編碼 ["date"]，是[一個完整的字串]，所以只有一個元素

操作行為上的差別
str 是不可改的 s = "hello" s[0] = "H" 這樣會報錯 TypeError: 'str' object does not support item assignment 
list 可以做更改 lst = ["hello"] lst[0] = "world" ， 查詢 lst 此時的結果為 world
---

