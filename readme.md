## 每週全國票房

[![Build Status](https://travis-ci.org/Phate334/box-office-tw.svg?branch=master)](https://travis-ci.org/Phate334/box-office-tw)

這個專案目標是取回 [Opendata](https://data.gov.tw/dataset/94224) 和 [TFI](https://www.tfi.org.tw/BoxOfficeBulletin/weekly) 公布的每週票房資料，並轉為 JSON 格式。

目前[首頁](https://phate334.github.io/box-office-tw/)顯示最新一週的資料，可以排序、過濾。

# API

所有資料都放在 [/docs](/docs) 目錄下，包括下載的原始資料及轉換過的 json 檔。

## JSON

- 資料索引
  - [https://phate334.github.io/box-office-tw/json/](https://phate334.github.io/box-office-tw/json/)

```json
["20190506-20190512"]
```

- 取出資料
  - [https://phate334.github.io/box-office-tw/json/20190506-20190512.json](https://phate334.github.io/box-office-tw/json/20190506-20190512.json)

```json
[
  {
    "序號": 1,
    "國別地區": "南韓",
    "中文片名": "親愛的仇人",
    "上映日期": "2019/05/04",
    "申請人": "可樂藝術文創股份有限公司",
    "出品": "M-Line Distribution",
    "上映院數": 14,
    "銷售票數": 966,
    "周票數變動率": "5,266.67%",
    "銷售金額": 217475,
    "累計銷售票數": 984,
    "累計銷售金額": 220515
  }
]
```

## Source data

- 資料索引

  - [https://phate334.github.io/box-office-tw/source/tfi/](https://phate334.github.io/box-office-tw/source/tfi/)
  - [https://phate334.github.io/box-office-tw/source/opendata/](https://phate334.github.io/box-office-tw/source/opendata/)

```json
{
  "20190513-20190519": {
    "pdf": "https://www.tfi.org.tw/Content/TFI/PublicInfo/全國票房2019年0513-0519統計資訊.pdf",
    "xlsx": "https://www.tfi.org.tw/Content/TFI/PublicInfo/全國票房2019年0513-0519統計資訊.xlsx"
  }
}
```

```json
{
  "20190506-20190512": {
    "csv": "https://opendata.culture.tw/upload/dataSource/2019-05-16/9b5f358f-9263-4cc7-b0cf-201ea4633680/994a6d972ceaa26f6356df4fb61cd60d.csv"
  }
}
```

- 取出資料

  - [https://phate334.github.io/box-office-tw/source/tfi/20190513-20190519.pdf](https://phate334.github.io/box-office-tw/source/tfi/20190513-20190519.pdf)
  - [https://phate334.github.io/box-office-tw/source/tfi/20190513-20190519.xlsx](https://phate334.github.io/box-office-tw/source/tfi/20190513-20190519.xlsx)
  - [https://phate334.github.io/box-office-tw/source/opendata/20190506-20190512.csv](https://phate334.github.io/box-office-tw/source/opendata/20190506-20190512.csv)

---

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
