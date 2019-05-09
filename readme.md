# 進度

目前[首頁](https://phate334.github.io/box-office-tw/)顯示最新一週的資料，可以排序、過濾。

# 資料清理

紀錄轉換成 json 過程額外處理的內容

1. 部分檔案開頭有 unicode BOM

   - source/opendata/20180730-20180805.csv
   - source/opendata/20180806-20180812.csv
   - source/opendata/20180813-20180819.csv
   - source/opendata/20180820-20180826.csv
   - source/opendata/20180827-20180902.csv
   - source/opendata/20180903-20180909.csv
   - source/opendata/20180910-20180916.csv
   - source/opendata/20180917-20180923.csv
   - source/opendata/20180924-20180930.csv
   - source/opendata/20181001-20181007.csv
   - source/opendata/20181008-20181014.csv

2. 每筆資料最後多一個逗點，被多判斷成一個空欄位

   - source/opendata/20180924-20180930.csv

放在數值轉換一起處理，刪除多餘的空欄位

3. 方便後續應用，票數、金額包括序號都去除逗號並轉為整數型態。

## 欄位定義

- column-defines.json

用在顯示 Ag-Grid 的設定檔。

- `票數變動率`的欄位名稱沒統一，目前還沒處理所以沒放進去。
  - 周票數變動率
  - 本周票數變動率
  - 票數變動率
  - 本周票數變動
  - 周票數變動率
  - 票數變動率
