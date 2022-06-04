from pytrends.request import TrendReq
import pandas as pd
path = '/var/log/history/' 

# self-define crawler
keywords = ['TSMC', '應用材料', 'ASML', 'SUMCO']
pytrend = TrendReq(hl='zh-TW')
pytrend.build_payload(kw_list=keywords, cat=0, timeframe='today 12-m', geo='TW', gprop='')
Timedf = pytrend.interest_over_time()
Timedf = Timedf.iloc[: , :-1]
filename = path + "data.csv"

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