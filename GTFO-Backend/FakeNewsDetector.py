import pandas as pd
from IE_Engine import *

def SiteTagger(SearchURL):
    df1 = pd.read_csv('websites.csv')
    fakeNewsList1 = list(df1['url'])
    # print(fakeNewsList1)
    df2 = pd.read_csv('news_sample.csv')
    df2 = df2[df2['domain']!='political']
    fakeNewsList2 = list(df2['domain'])
    # print(fakeNewsList2)

    fakeNewsList = list(set(fakeNewsList1+fakeNewsList2))
    # print(fakeNewsList)

    for fakeUrl in fakeNewsList:
        if fakeUrl in SearchURL:
            return ("Not a Trusted Site")

    return "No site info"

def ContentChecker():
    return True

def CheckNews(text):
    tokenOfText = IE_from_text(text.lower())
    # print(tokenOfText)

    FNdf_new = pd.read_csv("FalseNewsDataset_new.csv",header=0)
    Extracted_tokens_List=[]
    Counter = 0
    Counter2 = 0
    ResponseDf = pd.DataFrame(columns=['News','Tag','Link'])
    OpString = ""
    OpString2 = ""

    for i in range(len(FNdf_new['Extracted_tokens'])):
        Extracted_tokens = FNdf_new['Extracted_tokens'][i].replace('[','').replace(']','').replace('\'','').split(',')
        Extracted_tokens = [x.strip(' ') for x in Extracted_tokens]

        Similarity = len(Extracted_tokens) - len(set(Extracted_tokens) & set(tokenOfText))
        # print(Extracted_tokens)
        # print(set(Extracted_tokens) & set(tokenOfText))
        # print(Similarity)
        if Similarity < 1:
            if Counter==0:
                OpString+="This looks like its related to a FAKE news... \n\n"
            # print(Extracted_tokens)
            OpString= OpString+"News: " +FNdf_new['News'][i]+"\n"
            OpString= OpString+"The above news is tagged as: "+FNdf_new['Tag'][i]+"\n"
            OpString= OpString+"To know more click on this link: "+FNdf_new['NewsLink'][i]+"\n\n"
            # print()
            ResponseDf = ResponseDf.append(pd.DataFrame([[FNdf_new['News'][i], FNdf_new['Tag'][i], FNdf_new['NewsLink'][i]]], columns=ResponseDf.columns))

            Counter+=1

        if Similarity < 2 and len(Extracted_tokens)>2:
            if Counter2==0:
                OpString2+="This looks like its related to a FAKE news circulating regrading Corona Virus! Please find the below mentioned articles for clarification.....\n\n"
            # print(Extracted_tokens)
            OpString2= OpString2+"News: " +FNdf_new['News'][i]+"\n"
            OpString2= OpString2+"The above news is tagged as: "+FNdf_new['Tag'][i]+"\n"
            OpString2= OpString2+"To know more click on this link: "+FNdf_new['NewsLink'][i]+"\n\n"

            Counter2+=1

        Extracted_tokens_List.append(Extracted_tokens)
    if Counter==0:
        tag = "Not Fake!"
    else:
        tag = "Fake News!"

    return tag, OpString, OpString2

text1 = """Social media users have been sharing an image online that purports to be a screen grab of a news report claiming that the coronavirus has been found in crab legs. Examples can be seen  here  and  here .

The screen grab image appears to have been created with an application called “News Maker – Create The News.” It is available on the Apple App Store and provides different options for styles and fake news station names.

The first screenshot of the app shows a "News 6" template ( here ).

The description of the app reads: “News Maker is the only app that lets you create your own realistic, television-style news screenshots using your own photos and your own creative headlines! Amaze your friends and family when you share a fun news image where you are the star! Let your imagination run wild while you make the news with News Maker.”

A reverse Google image search shows that the image of the crab legs appears to be a widely used stock photograph. It can be seen on the websites of various seafood stores. Examples here and  here .

At the beginning of the coronavirus outbreak, coronavirus was tied to a live animal and seafood market in Wuhan, China. This suggested an animal-to-person transmission ( here ).

Both the U.S. Food and Drug Administration and the Centers for Disease Control say food is not connected to coronavirus transmission:  

"Currently there is no evidence of food or food packaging being associated with transmission of COVID-19. Unlike foodborne gastrointestinal (GI) viruses like norovirus and hepatitis A that often make people ill through contaminated food, SARS-CoV-2, which causes COVID-19, is a virus that causes respiratory illness. Foodborne exposure to this virus is not known to be a route of transmission" ( more here ).

The CDC says transmission is unlikely for refrigerated or frozen foods, a common method of distribution for seafood: “In general, because of poor survivability of these coronaviruses on surfaces, there is likely very low risk of spread from food products or packaging that are shipped over a period of days or weeks at ambient, refrigerated, or frozen temperatures.”

The CDC advises practicing general food safety by washing hands for at least 20 seconds with soap and water before preparing or eating food ( here ).

This claim is therefore false. The news story image in the claim was fabricated and the FDA and CDC say there is no evidence that the coronavirus can be transmitted through food.
"""
text2="""Transmission via mosquito bites
Although it’s always appropriate to keep a safe distance from the insect that spreads paludism and dengue fever, respiratory viruses don’t seem, at this stage, to be transmitted by mosquito bites, but by droplets of saliva or nasal secretions expelled by an infected person when coughing or sneezing. Speaking of animals, no house pets seem to have been infected by the new coronavirus.
"""

text3 = """Breaking News from CNN :-
Dr. Li Wenliang, China's hero doctor who was punished for telling the truth about Corona Virus and later died due to the same disease, had documented casefiles for research purposes and had in the casefiles proposed a cure that would significantly decrease the impact of the COVID - 19 Virus on the human body. The chemical Methylxanthine, Theobromine and Theophylline stimulate compounds that can ward off these virus in a human with atleast an average immune system. Whats more shocking is that these complex words that were so difficult for people in China to understand is actually called Tea in India, YES, our regular Tea has all these chemicals already in it. The main Methylxanthine in tea is the stimulant caffeine. Other Methylxanthines found in tea are two chemically similar compounds, Theobromine and Theophylline. The tea plant creates these chemicals as a way to ward off insects and other animals. Who would have known that all the solution to these virus would be a simple cup of TEA. and that is the reason so many patients in China are being cured. The hospital staff in china has started serving tea to the patients 3 times a day, And the effect is finally in Wuhan "The centre of this Pandemic" has been contained and community transmission has almost stopped.
Please Share this message to your friends and family to make them aware about this blessing in the form of TEA in your kitchen.
Forwarded as received."""

text4 = """India had 2,547 confirmed coronavirus cases until Friday and the death toll climbed to 62 as Prime Minister Narendra Modi asked citizens to show their "collective resolve” in fighting the disease that has prompted his government to impose a three-week lockdown. "In that brightness, we should resolve that we are not alone. Nobody is alone," Modi said.
"""



# print(CheckNews(text4))