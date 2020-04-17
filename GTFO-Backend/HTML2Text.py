import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import IE_Engine
from selenium import webdriver
import time

SaveReportsIn = "C:\\Users\\91904\\Desktop\\Project2 WebScrapper\\ReportDownload"
chromedriver = "C:\\Users\\91904\\Downloads\\chromedriver_win32\\chromedriver.exe"

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : SaveReportsIn}
chromeOptions.add_experimental_option("prefs",prefs)


def ExtractData():
    FalseNewsDf = pd.DataFrame(columns=['News', 'Tag', 'NewsLink'])
    TotalDataList = []
    for i in range(1,77):

        url = "https://www.poynter.org/ifcn-covid-19-misinformation/page/"+str(i)+"/?search_terms=Corona"

        driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)
        driver.get(url)

        code= driver.page_source
        # print(code)
        soup_doc = BeautifulSoup(code, 'html.parser')
        # print(soup_doc.prettify())
        for h2content in soup_doc.find_all('h2'):
            text = str(h2content)
            print(text)
            InfoExtractRegex = re.compile(r'</span>(.|\n)*?</a>')
            # OriginalNewsTag = re.compile(r'href=\"(.|\n)*? rel=')
            # OriginalNewsTag =re.compile(r"""(?<=(<a href=))(\w|\d|\n|[().,\-:;@#$%^&*\[\]"'+–/\/®°⁰!?{}|`~]| )+?(?=(rel=))""")
            Tag = re.compile(r"""(?<=(>))(\w|\d|\n|[().,\-:;@#$%^&*\[\]"'+–/\/®°⁰!?{}|`~]| )+?(?=(</span>))""")

            start = text.find("a href=") + len("a href=")
            end = text.find(" rel=")
            Link = text[start:end]

            Info = InfoExtractRegex.search(text)
            Tag = Tag.search(text)
            # NewsLink= OriginalNewsTag.search(text)
            News = Info.group().replace('</span>', '').replace('</a>', '').strip()
            tag = Tag.group().replace('</span>', '').replace('</a>', '').replace(':', '').strip()
            NewsLink = Link[1:-1]
            DataList = [News, tag, NewsLink]
            TotalDataList.append(DataList)
            FalseNewsDf = FalseNewsDf.append({'News': News, 'Tag': tag, 'NewsLink': NewsLink}, ignore_index=True)
            print(DataList)
        driver.close()

    # print(type(str(soup_doc.find_all('h2')[0])))
    FalseNewsDf.to_csv('FalseNewsDataset.csv', index=False)


def AddTokensToData():
    dropdataList=["(Org. doesn't apply rating)","Correct","Manipulation","PANTS ON FIRE","Pants on Fire!","Pseudoscience, fake news, disinformation","MOSTLY TRUE","Questionable"]

    FNdf_new = pd.read_csv("FalseNewsDataset.csv",header=0)
    FNdf = FNdf_new.drop(FNdf_new[(FNdf_new['Tag'] == "(Org. doesn't apply rating)") | (FNdf_new['Tag'] == "Correct")| (FNdf_new['Tag'] == "Explanatory") | (FNdf_new['Tag'] == "Manipulation") | (FNdf_new['Tag'] == "PANTS ON FIRE") | (FNdf_new['Tag'] == "Pants on Fire!") | (FNdf_new['Tag'] == "Pseudoscience, fake news, disinformation") | (FNdf_new['Tag'] == "MOSTLY TRUE") | (FNdf_new['Tag'] == "Questionable")].index)

    NewsList=list(FNdf['News'])
    print(len(NewsList))
    IeList=[]


    for news in NewsList:
        # print(news)
        # print(IE_from_text(news))
        IeList.append(IE_Engine.IE_from_text(news))

    print(len(IeList))
    FNdf['Extracted_tokens']= IeList
    FNdf.to_csv('FalseNewsDataset_new.csv', index=False)

# ExtractData()
AddTokensToData()