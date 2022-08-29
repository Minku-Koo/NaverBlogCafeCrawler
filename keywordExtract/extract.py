
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import nltk

def readRawData(filename):
    with open('../output/rawData/' + filename + '.txt') as f:
        data = f.read()
    return data

def mecabProcess(data):
    # mecab preprocess
    # only 동사 명사 형용사
    return 

def getWordFrequency(data):
    # word freaquency calculation
    # create graph
    # create result text file
    return 

def getWordCloud(data, title, imsize):
    # create worldcloud
    word_max = 100
    wordcloud = WordCloud(font_path='./font/BMDOHYEON_ttf.ttf', 
                            background_color='white',
                            max_words=word_max,
                            max_font_size=200,
                            height=700,
                            width=900).generate(data)
    plt.figure(imsize) #이미지 사이즈 지정
    plt.imshow(wordcloud, interpolation='lanczos') #이미지의 부드럽기 정도
    plt.axis('off') #x y 축 숫자 제거
    plt.savefig('../result-graph/word-cloud/'+title+'-wordcloud.png', dpi=300)
    return 



def doKeybert():
    # using keybert model
    # keyword extraction
    # make graph
    # create result text file
    return 

