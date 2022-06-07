from pytrends.request import TrendReq
import pandas as pd


class GoogleCrawler():
    def __init__(self, keywords):
        self.keywords = keywords
    def get_trend(self):
        pytrend = TrendReq(hl='zh-TW')
        pytrend.build_payload(kw_list=self.keywords, cat=0,\
                              timeframe='today 12-m', geo='TW', gprop='')
        Timedf = pytrend.interest_over_time()
        Timedf = Timedf.iloc[: , :-1]
        return Timedf



if __name__ == "__main__":
    path = '/sample_crawler/history/' 
    filename = path + "data.csv"
    keywords = ['TSMC', '應用材料', 'ASML', 'SUMCO']
    
    crawler = GoogleCrawler(keywords)
    Timedf = crawler.get_trend()

    try:
        print("Save to pvc")
        Timedf.to_csv(filename , index=False)
    except:
        print("Save Error, Change")
        print("Save to Root")
        Timedf.to_csv("data.csv")
    print('CSV is OK')

    # Filtered by regions
    '''
    Region_df = pytrend.interest_by_region()
    Region_df = Region_df.sort_values(['TSMC'],ascending=False)
    Region_df.to_csv("Regiontrend.csv")
    '''