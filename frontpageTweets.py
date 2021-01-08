#Class which will pull the relevant Tweets

import requests
import json
import datetime

#TODO make this a filtered stream: https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/master/Filtered-Stream/filtered_stream.py

def getTodaysTweets():
    url = create_url()
    headers = create_headers()
    json_response = connectToTwitter(url, headers)
    print(json.dumps(json_response, indent=4, sort_keys=True))


def create_url():
    oneDayAgo = datetime.datetime.today() - datetime.timedelta(days=1, hours=8)
    query = "(from:AllieHBNews OR from:hendopolis OR from:BBCHelena) TomorrowsPapersToday -is:retweet has:images&max_results=30&start_time=" + oneDayAgo.isoformat() + "Z"
    tweet_fields = "tweet.fields=attachments,author_id"
    media_fields = "media.fields=height,url,width"
    #TODO need to pull more attributes to get the images: https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}&{}".format(query, tweet_fields, media_fields)
    print(url)
    return url

def create_headers():
    f = open('twitterKey.json', 'r')
    creds = json.load(f)
    headers = {"Authorization": "Bearer {}".format(creds["bearertoken"])}
    f.close()
    return headers


def connectToTwitter(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()