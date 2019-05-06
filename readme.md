# 資料清理

紀錄轉換成 json 過程額外處理的內容

1. 部分檔案開頭有 unicode BOM

    * source/opendata/20180730-20180805.csv
    * source/opendata/20180806-20180812.csv
    * source/opendata/20180813-20180819.csv
    * source/opendata/20180820-20180826.csv
    * source/opendata/20180827-20180902.csv
    * source/opendata/20180903-20180909.csv
    * source/opendata/20180910-20180916.csv
    * source/opendata/20180917-20180923.csv
    * source/opendata/20180924-20180930.csv
    * source/opendata/20181001-20181007.csv
    * source/opendata/20181008-20181014.csv

2. 每筆資料最後多一個逗點，被多判斷成一個空欄位

    * source/opendata/20180924-20180930.csv

放在數值轉換一起處理，刪除多餘的空欄位
