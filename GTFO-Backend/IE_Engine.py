from nltk.corpus import stopwords
import pandas as pd
import nltk
# nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

ps = PorterStemmer()

lemmatizer = WordNetLemmatizer()

def IE_from_text(text):

    text_tokens = word_tokenize(text)
    text_tokens = [i for i in text_tokens if i.isalnum()]
    newStopwordsList = ['claim','claiming','video','audio','circulating','whatsapp','post','social','media','saying','text','message','viral','corona','coronavirus','has','had','have']

    new_stopwords= set(newStopwordsList)
    stop_words = set(stopwords.words('english'))
    stop_words.update(new_stopwords)
    text_tokens = [w for w in text_tokens if not w in stop_words]
    tags = nltk.pos_tag(text_tokens)

    # print(tags)
    extracted_words1 = [ps.stem(word).lower() for word,pos in tags if (pos == 'NNS' or pos == 'NNPS')]
    extracted_words2 = [word.lower() for word,pos in tags if (pos == 'NN' or pos == 'NNP' or pos == 'VBG' or pos == 'VB' or pos=='VBN' or pos=='VBD')]
    extracted_words3 = [lemmatizer.lemmatize(word).lower() for word, pos in tags if (pos == 'VBZ')]
    extracted_words = extracted_words1 + extracted_words2 + extracted_words3


    filtered_tokens = [w for w in extracted_words if not w in stop_words]
    # print(filtered_tokens)
    return filtered_tokens

# print(IE_from_text("Mosquitoes can spread the coronavirus?"))

