import matplotlib.pyplot as plt
from wordcloud import WordCloud


# Takes the full conversation_history and returns a list of the message text
def historyToList(history) -> list:
    msg_list = []
    for msg in history:
        msg_list.append(msg['text'])

    return msg_list


# TODO define logic to scan messages for tag keys and group into dictionary
def makeCloud(msg_list, tag_dict):
    unique_string = " ".join(msg_list)
    print(msg_list)
    print(unique_string)
    wordcloud = WordCloud(width=1000, height=500).generate(unique_string)
    plt.figure(figsize=(15, 8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig("your_file_name" + ".png", bbox_inches='tight')
    plt.show()
    plt.close()