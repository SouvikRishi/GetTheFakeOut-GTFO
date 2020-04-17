# GetTheFakeOut-GTFO
A webapp and chrome extension for COVID-19 related fake news identifier 

## Inspiration
The current increase of fake news in times of a global pandemic instills fear and tension amongst the normal people. So, we came up an user friendly, easy to install chrome extension where you just copy and paste the text from a website and it returns you, whether the news is fake or not in no time.

## What it does
1. It takes an certain selected text from the browser as input to the extension.
2. It goes through a fact checking algorithm related to COVID-19 in the background and returning the result back to the user.
3. The result consists of tags such as Clickbait, related fake news, primary source and the corrected statement from a trusted source.
4. The main highlight here is the user-friendly nature of the extension which scaled up to Enterprise level.

## How we built it
1. The front-end consists of a Google Chrome extension as a user-facing interface built with HTML5, CSS3, Javascript and JQuery.
2. The middle layer consists of Flask framework which holds the COVID-19 algorithm and provides a link to the RESTful APIs 
3. The data is fetched using post() method which hold the API for the server.

## Accomplishments that we're proud of
We actually got the project working! This was quite an endeavor for us as we ran into quite a few issues early on. Luckily we were able to power through two nights, fixing each issue along the way (thanks StackOverflow!). This was the first hackathon for most of our group, so having a tangible result is really cool. Plus this is something that we wouldn't mind working on some more after the hackathon to see how far we can take it.

## What we learned
We learned a lot during this Hackathon! None of us were very familiar with any of the technologies we implemented for our project. Some of us did not even know Python. When we were coming up with the idea and implementation, we all wanted to work on bettering our understanding with some of the platforms and tools we used. Over the past 48 hours, we've been able to get hands-on experience using Python, Flask, HTML,CSS, Javascript, and a variety of other languages and libraries. This project was very involved for us, and left us with some valuable experience we can build upon in the future.

## What's next for GTFO
1. Future down the line we like to enhance the scale of the application to broader spectrum of social media such as Facebook, Twitter, Instagram.
2. Will specially like to tap into Messenger and automated chatbots which filters out the fake news related to COVID- 19 thereby increasing the social harmony to a level of negligible human interaction with fraudulent data. 
