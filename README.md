### Slack Scraper

This application will scrape a Slack channel and extract the contents of a Slack channel and create a wordcloud based on the presence of collection of tags.

# Requirements

You will need to create a config.ini file in the parent directory matching the following format.
```[slack]
channel_id = <channel_id>
starting_ts = 0
token = <botToken>```