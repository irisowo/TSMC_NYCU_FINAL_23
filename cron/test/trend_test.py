from asyncio import TimerHandle
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import trend

import pandas.api.types as ptypes

def test_get_trend_cols():
    keywords = ['TSMC', '應用材料', 'ASML', 'SUMCO']
    crawler = trend.GoogleCrawler(keywords)
    Timedf = crawler.get_trend()
    assert Timedf.columns.tolist() == ['TSMC', '應用材料', 'ASML', 'SUMCO']

def test_get_trend_lens():
    keywords = ['TSMC', '應用材料', 'ASML', 'SUMCO']
    crawler = trend.GoogleCrawler(keywords)
    Timedf = crawler.get_trend()
    for col in keywords:
        row = Timedf[col]
        assert len(row) == 365//7


def test_get_trend_type():
    keywords = ['TSMC', '應用材料', 'ASML', 'SUMCO']
    crawler = trend.GoogleCrawler(keywords)
    Timedf = crawler.get_trend()
    assert all(ptypes.is_numeric_dtype(Timedf[col]) for col in keywords)