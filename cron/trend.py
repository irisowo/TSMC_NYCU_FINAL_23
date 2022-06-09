from pytrends.request import TrendReq
path = '/sample_crawler/history/' 
keywords = ['TSMC', '應用材料', 'ASML', 'SUMCO']

class GoogleCrawler():
    def __init__(self, keywords):
        self.keywords = keywords

    def get_trend(self):
        # get data
        pytrend = TrendReq(hl='zh-TW')
        pytrend.build_payload(kw_list=self.keywords, cat=0,\
                              timeframe='today 12-m',\
                              geo='TW', gprop='')
        Timedf = pytrend.interest_over_time()
        Timedf = Timedf.iloc[: , :-1]
        
        # save file
        filename = path + "data.csv"
        try:
            print("Save to pvc")
            Timedf.to_csv(filename , index=False)
        except:
            print("Save Error")

        print('CSV is OK')
        return Timedf


if __name__ == "__main__":
    crawler = GoogleCrawler(keywords)
    Timedf = crawler.get_trend()