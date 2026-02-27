Question:
       1
     2 3
   4 5 6
7 8 9 10 

"""
原先思考邏輯
1.使用到 for 迴圈
2.一個 for 迴圈列印出空格
3.另一個 for 迴圈列印出數字
4.由於空格與數字需同時列印出，所以 還需要一個 for 迴圈用來控制這兩個 for 全圈
5.共用到三個 for 迴圈
"""

"""
GPT 指導
1.首先先觀察規律，先分析結構
2.觀察有幾列  # 4列
3.每一列當中出現幾個數字，第一列 1 個，第二列 2 個...，所以數字規律是 第 n 列會列印出 n 個數字
4.那每一列有幾個空格，第一列 3 個，第二列 2 個...，所以空格規律是 第 n 列空格 = 總列數 - n
5.思考 for 迴圈的設計結構，最外層 for 用來控制列數，內層 for 用來控制空格，內層 for 用來控制列印出來的數字
"""

"""
當程式不知道該從哪下手，東一片西一片時，「先寫骨架」再補剩下的內容
圖形題目的萬用起手式
1.第一步，先寫外層迴圈
  """
  rows = 4

  for i in range(1, rows + 1):
      print(i)
    
  總共跑四行，for i in range(1, 5)
  range(a, b) 的意思是：從 a 開始到 b 之前（不包含 b）
  """
2.第二步，先釐清每一列要做什麼
  每一列會做兩件事情 1.印空格 2.印數字
  """
  for i in range(1, rows + 1):
    # 印空格
    # 印數字的次數
    print(i)
  """
3.把規律轉成功式
  3.1已知第 n 列空格 = 總列數 - n，所以當 i 從一開始，空格數為 rows - i 
  """
  for space in range(rows - i):
        print("  ", end=" ")
  為什麼這邊多了 end=""，因為在 Python 中預設會自動換行，也就是說預設為 print(" " * (rows - i), end="\n")
  但又因後面還需要加上數字，所以此時還不能讓其換行，所以改成空字串
  """
  3.2已知第 n 列會列印出 n 個數字，所以第 i 列印 i 個數字
  """
  num = 1 
  for number in ranage((i):
        print(num , end=" ")
        num += 1 
  """         

"""
所以最終的程式碼為
num = 1
rows = 4

for i in range(1, rows + 1):

    # 印空格
    for space in range(rows - i):
        print("  ", end="")

    # 印數字
    for j in range(i):
        print(num, end=" ")
        num += 1

    print()  # 換行
"""


