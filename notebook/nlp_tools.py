import re
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import spacy
from spacy.lang.fr.stop_words import STOP_WORDS
import string
from vaderSentiment_fr.vaderSentiment import SentimentIntensityAnalyzer


def clean_text(text):

    text = text.lower()
    text = text.replace('\n', ' ').replace('\r', '')
    text = ' '.join(text.split())
    text = re.sub(r"[A-Za-z\.]*[0-9]+[A-Za-z%°\.]*", "", text)
    text = re.sub(r"(\s\-\s|-$)", "", text)
    text = re.sub(r"[,\!\?\%\(\)\/\"]", "", text)
    text = re.sub(r"\&\S*\s", "", text)
    text = re.sub(r"\&", "", text)
    text = re.sub(r"\+", "", text)
    text = re.sub(r"\#", "", text)
    text = re.sub(r"\$", "", text)
    text = re.sub(r"\£", "", text)
    text = re.sub(r"\%", "", text)
    text = re.sub(r"\:", "", text)
    text = re.sub(r"\@", "", text)
    text = re.sub(r"\-", "", text)

    return text


def preprocessing_data(data):

    data["Comment"] = data["Comment"].apply(clean_text)
    data["Comment"]= data["Comment"].str.lower()

    AComment=[]
    for comment in data["Comment"].apply(str):
        Word_Tok = []
        for word in  re.sub("\W"," ",comment ).split():
            Word_Tok.append(word)
        AComment.append(Word_Tok)
    data["Word_Tok"]= AComment

    stop_words=set(STOP_WORDS)

    deselect_stop_words = ['n\'', 'ne','pas','plus','personne','aucun','ni','aucune','rien']
    for w in deselect_stop_words:
        if w in stop_words:
            stop_words.remove(w)
        else:
            continue
            
    AllfilteredComment=[]
    for comment in data["Word_Tok"]:
        filteredComment = [w for w in comment if not ((w in stop_words) or (len(w) == 1))]
        AllfilteredComment.append(' '.join(filteredComment))
    data["CommentAferPreproc"]=AllfilteredComment

    return data 


def find_sentiments(data):
    SIA = SentimentIntensityAnalyzer()
    senti_list = []
    for n, i in enumerate(data["CommentAferPreproc"]):
        vs = SIA.polarity_scores(i)
        senti_list.append( [data.date.iloc[n],vs['neg'], vs['neu'], vs['pos']])

    return pd.DataFrame(senti_list, columns=["date","très négatif", "négatif", "légèrement négatif" ])

