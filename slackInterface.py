import logging

# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def getConversationHistory(token, channel_id, oldest):
    # WebClient instantiates a client that can call API methods
    # When using Bolt, you can use either `app.client` or the `client` passed to listeners.
    client = WebClient(token=token)
    logger = logging.getLogger(__name__)
    try:
        # Call the conversations.history method using the WebClient
        # https://api.slack.com/methods/conversations.history$pagination
        result = client.conversations_history(channel=channel_id, oldest=oldest)

        if result['messages']:
            return result["messages"]
        else:
            return None

    except SlackApiError as e:
        logger.error("Error creating conversation: {}".format(e))

    # https://www.datacamp.com/tutorial/wordcloud-python
