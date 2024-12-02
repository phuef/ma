# file to generate a wordCloud of the HTML's
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from modules import DB
from bs4 import BeautifulSoup
from tqdm import tqdm


dbEmbeddings =DB('websites', "embeddings")

# Generate a word cloud image
def generateWordCloudForText(text):
    wordcloud = WordCloud(background_color="white", collocations=False).generate(text)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

def getHtmlForType(type, db):
    html=''
    websites = db.find({'real_type': type})
    for website in tqdm(websites):
        # Remove the html tags and only get the text in return
        soup = BeautifulSoup(website['html_code'], 'html.parser')
        text_only = soup.get_text()
        html+=text_only +' '
    return html

def getHtmlForTypeWithTags(type, db):
    html=''
    websites = db.find({'real_type': type})
    for website in tqdm(websites):
        text=website['html_code']
        html+=text +' '
    return html

#text=getHtmlForType('IGV', dbEmbeddings)
text=getHtmlForTypeWithTags('IGV', dbEmbeddings)
generateWordCloudForText(text)