from pytrends.request import TrendReq
import pandas as pd


keywords = ['TSMC', '應用材料', 'ASML', 'SUMCO']
pytrend = TrendReq(hl='zh-TW')

# Timetrend
pytrend.build_payload(kw_list=keywords, cat=0, timeframe='today 12-m', geo='TW', gprop='')
Timedf = pytrend.interest_over_time()
Timedf = Timedf.iloc[: , :-1]
Timedf.to_csv("Timetrend.csv")


# Filtered by regions
Region_df = pytrend.interest_by_region()
Region_df = Region_df.sort_values(['TSMC'],ascending=False)
Region_df.to_csv("Regiontrend.csv")