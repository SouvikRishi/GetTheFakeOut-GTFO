import requests

text2="""Transmission via mosquito bites
Although it’s always appropriate to keep a safe distance from the insect that spreads paludism and dengue fever, respiratory viruses don’t seem, at this stage, to be transmitted by mosquito bites, but by droplets of saliva or nasal secretions expelled by an infected person when coughing or sneezing. Speaking of animals, no house pets seem to have been infected by the new coronavirus.
"""

text = """Social media users have been sharing an image online that purports to be a screen grab of a news report claiming that the coronavirus has been found in crab legs. Examples can be seen  here  and  here .

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

text4 = """India had 2,547 confirmed coronavirus cases until Friday and the death toll climbed to 62 as Prime Minister Narendra Modi asked citizens to show their "collective resolve” in fighting the disease that has prompted his government to impose a three-week lockdown. "In that brightness, we should resolve that we are not alone. Nobody is alone," Modi said.
"""

res1 = requests.post('http://localhost:5001/', json={"NewsText":text2})

if res1.ok:
    print(res1.json())

res2 = requests.post('http://localhost:5001/urlCheck', json={"URL":'cbsnews.com.co'})
if res2.ok:
    print(res2.json())