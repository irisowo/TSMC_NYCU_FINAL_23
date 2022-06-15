﻿import requests
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from pytrends.request import TrendReq

# nltk.download('popular')
path = '/sample_crawler/history/' 

class GoogleCrawler():
    
    def __init__(self):
        self.url = 'https://www.google.com/search?q='    
    #  URL 萃取 From Google Search上 , using 第三方套件
    #  https://python-googlesearch.readthedocs.io/en/latest/
    def google_url_search_byOpenSource(query,tbs='qdr:m',num=10):
        array_url = [url for url in search('tsmc', tbs='qdr:m' , num=10)]
        return array_url
    # 網路擷取器
    def get_source(self,url):
        try:
            session = HTMLSession()
            response = session.get(url)
            return response
        except requests.exceptions.RequestException as e:
            print(e)
    # URL 萃取 From Google Search上
    def scrape_google(self,query):

        response = self.get_source(self.url + query)
        links = list(response.html.absolute_links)
        google_domains = ('https://www.google.', 
                          'https://google.', 
                          'https://webcache.googleusercontent.', 
                          'http://webcache.googleusercontent.', 
                          'https://policies.google.',
                          'https://support.google.',
                          'https://maps.google.')

        for url in links[:]:
            if url.startswith(google_domains):
                links.remove(url)
        return links
    
# URL萃取器，有link之外，也有標題
#     qdr:h (past hour)
#     qdr:d (past day)
#     qdr:w (past week)
#     qdr:m (past month)
#     qdr:y (past year)
    def google_search(self,query,timeline='',page='0'):
        url = self.url + query + '&tbs={timeline}&start={page}'.format(timeline=timeline,page=page)
        print('[Check][URL] URL : {url}'.format(url=url))
        response = self.get_source(url)
        return self.parse_googleResults(response)
    # Google Search Result Parsing
    def parse_googleResults(self,response):

        css_identifier_result = "tF2Cxc"
        css_identifier_title = "h3"
        css_identifier_link = "yuRUbf"
        css_identifier_text = "VwiC3b"
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.findAll("div", {"class": css_identifier_result})
        output = []
        for result in results:
            item = {
                'title': result.find(css_identifier_title).get_text(),
                'link': result.find("div", {"class": css_identifier_link}).find(href=True)['href'],
                'text': result.find("div", {"class": css_identifier_text}).get_text()
            }
            output.append(item)
        return output
    
    # 網頁解析器
    def html_parser(self,htmlText):
        soup = BeautifulSoup(htmlText, 'html.parser')
        return soup
    # 解析後，取<p>文字
    def html_getText(self,soup):
        orignal_text = ''
        for el in soup.find_all('p'):
            orignal_text += ''.join(el.find_all(text=True))
        return orignal_text
    
    def word_count(self, text):
        counts = dict()
        stop_words = set(stopwords.words('english'))
        words = word_tokenize(text)
        #words = text.replace(',','').split()
        for word in words:
            if word not in stop_words:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1
        return counts
    def get_wordcount_json(self,whitelist , dict_data):
        data_array = []
        for i in whitelist:
            json_data = {
                'Date' : 'Week1',
                'Company' : i , 
                'Count' : dict_data[i]
            }
            data_array.append(json_data)
        return data_array
    def jsonarray_tocsv(self,data_array,path):
        df = pd.DataFrame(data=data_array)
        filename = path + "crawler_result.csv"
        print("save result as " + filename)
        try:
            print("Save to pvc")
            df.to_csv(filename , index=False)
        except:
            print("Save Error, Change")
            print("Save to Root")
            df.to_csv("crawler_result.csv" , index=False)
        return
    
if __name__ == "__main__":
    query = "TSMC ASML"
    crawler = GoogleCrawler()
    results = crawler.google_search(query , 'qdr:w' , '10')
    print(results[:3])
    Target_URL = 'https://taipeitimes.com/News/biz/archives/2022/01/20/2003771688'
    response = crawler.get_source(Target_URL)
    soup = crawler.html_parser(response.text)
    orignal_text = crawler.html_getText(soup)
    print(orignal_text[:100])
    result_wordcount = crawler.word_count(orignal_text)
    result_wordcount
    whitelist = ['ASML' , 'Intel']
    end_result = crawler.get_wordcount_json(whitelist , result_wordcount)
    print(end_result)
    crawler.jsonarray_tocsv(end_result, path)
    
    # self-define crawler
    keywords = ['TSMC', '應用材料', 'ASML', 'SUMCO']
    pytrend = TrendReq(hl='zh-TW')
    pytrend.build_payload(kw_list=keywords, cat=0, timeframe='today 12-m', geo='TW', gprop='')
    Timedf = pytrend.interest_over_time()
    Timedf = Timedf.iloc[: , :-1]
    filename = path + "crawler_data.csv"
   
    try:
        print("Save to pvc")
        Timedf.to_csv(filename , index=False)
    except:
        print("Save Error, Change")
        print("Save to Root")
        Timedf.to_csv("crawler_data.csv")

    print('CSV is OK')