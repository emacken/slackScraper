import logging
import configparser

import conversationProcessor
import slackInterface

global config


# Updates our config.ini file with the value returned from findNewStartingTS
def updateConfig(starting_ts):
    config.set('slack', 'starting_ts', str(starting_ts))
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


# finds the timestamp of the latest message in the desired channel
def findNewStartingTS(messages):
    latest_ts = 0
    for msg in messages:
        print(msg['text'])
        if msg['ts'] is messages[0]['ts']:
            latest_ts = msg['ts']
    return latest_ts


if __name__ == "__main__":
    # define our configuration parser from 'config.ini'
    config = configparser.ConfigParser()
    config.read('config.ini')

    # calls the slackInterface module to retrieve the conversation history from the channel specified in the config
    conversation_history = slackInterface.getConversationHistory(config.get('slack', 'token'), config.get('slack', 'channel_id'), config.get('slack', 'starting_ts'))
    if conversation_history:
        updateConfig(findNewStartingTS(conversation_history))  # Update our config file with the new starting timestamp.
    else:
        print("No new messages!")

    print(conversation_history)
    conversationProcessor.makeCloud(conversationProcessor.historyToList(conversation_history))



