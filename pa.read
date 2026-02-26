-
假設 csv 檔案中的內容是
date,sales
2024-01-01,100
2024-01-02,120
---

--
DataFrame 物件內部有很多屬性
│
├── index (RangeIndex 0,1,2,...)
├── columns
│   ├── "date"  (dtype = object)
│   └── "sales" (dtype = int64)
├── dtypes
├── values
└── methods (head, mean, etc.)
---

--
data = pa.read_csv("scale.csv")
#Step 01 有一個檔案名為 "scale.csv" 被放在硬碟裡，此時不在記憶體當中，目前都還是一個靜態檔案
#Step 02 當程式碼執行 data = pd.read_csv("sales.csv") 會發生三件事情
#Step 03 Python 的 Pandas 會去 C 槽將 C:\sales.csv 的檔案經過讀取、解碼、解析、結構化  ⚠這時候讀取出來的內容字串形式的
#Step 04 此時 Pandas 套件會自動在「記憶體」中建立一個 DataFrame 物件，並 1.解析逗號 2.建立欄位名稱 3.建立資料列 4.建立 index 等
#Step 05 Python 的變數不是用來儲存資料，而是用來指向物件，假設當初所建立之 DataFrame 物件占用記憶體的位址是 0x1000 
#Step 06 則宣告的 data 之變數會被綁定在這個物件上面
---

--
當執行 data = pa.read_csv("scale.csv") 時，會發生
1.讀取第一行，也就是檔案中的 date,sale，此時 date 與 sales 的資料型態為 Object(字串)
2.程式碼 data = pd.read_csv("sales.csv", parse_dates=["date"], index_col="date")
3.透過 Keyword Argument（關鍵字參數）parse_dates = ["date"] 之後
4.在建立 DataFrame 的同時，就會將 date 的欄位解析成 datetime64[ns]
5.此時 DataFrame 的結構就會變成

  DataFrame 物件內部屬性
  │
  ├── index (RangeIndex 0,1,2,...)
  ├── columns
  │   ├── "date"  (dtype = datetime64[ns])  # numpy datetime64 型別
  │   └── "sales" (dtype = int64)
  ├── dtypes
  ├── values
  └── methods (head, mean, etc.)

6.當 dtype 改變代表 ．物件內部儲存方式改變 ．該欄位可以使用 datetime 的專屬方法 ．記憶體中不再是字串 array，而是時間型別 array
7.index_col="date" 意思是將 date 欄位從 DataFrame 物件內部屬性 Columns 中移出並建立成 Index 物件

  此時 DataFrame 物件內部屬性
      ├── Index = DatetimeIndex
      ├── Columns = ["sales"]
      ├── sales dtype = int64
      └── date 已不存在於 columns（成為 index）
8.做完這些都不會改變到內部的變數 data，只改變 read_csv 建立DataFrame 物件的內部結構
⚠資料型別轉換應該在結構調整之前
---

-













