import matplotlib.pyplot as plt
from wordcloud import WordCloud


def historyToList(history):
    msgList = []
    for msg in history:
        msgList.append(msg['text'])

    print(msgList)
    return msgList


def makeCloud(msgList):
    unique_string = (" ").join(msgList)
    wordcloud = WordCloud(width=1000, height=500).generate(unique_string)
    plt.figure(figsize=(15, 8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig("your_file_name" + ".png", bbox_inches='tight')
    plt.show()
    plt.close()