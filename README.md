# TSMC NYCU Final Project
## Frontend
- React.js
- docker image
    - `ginnycosine/react:v1`
- 將從後端傳來的資料渲染成網頁，並繪製圖表

## Backend
- Python flask
- docker image
    - `ginnycosine/flask:v5`
- 讀取 crawler 爬到的爬到的聲量趨勢，回傳資料至前端

## Crawler
- pytrend + cron
- docker image
    - `irisowo/cron:1day`
- 利用 cron 排程每天爬 google trend
- 此 pod 掛載於 pvc

## Webpage
- [Link](http://34.81.219.181:3000/trend)

## Structure
![](https://i.imgur.com/GXD9wKX.png)