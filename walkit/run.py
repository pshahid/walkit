from datetime import datetime
import requests
import praw
from ingest.crawler import crawled
from ingest.requestors import AuthenticatedRequestor

INI_NAME = 'walkit_backend'
USER_AGENT_STR = 'walkit - gathering a subreddit list'
HOSTNAME = 'localhost'
PORT = ':8000'


def add_if_absent(**kwargs):
    payload = {
        'name': kwargs['name'],
        'subscribers': kwargs['subscribers'],
        'created_date': kwargs['created'],
        'last_updated_date': str(datetime.utcnow()),
        'public_description': kwargs.get('public_description'),
        'sidebar_description': kwargs.get('sidebar_description')
    }
    response = requests.post('http://{0}{1}/api/v1/subreddit/'.format(HOSTNAME, PORT),
                             params={'format': 'json'}, json=payload)

    if 199 < response.status_code < 300:
        print(response.status_code)
    else:
        print(response.status_code)
        print(response.content)


def main():
    reddit = praw.Reddit(INI_NAME, user_agent=USER_AGENT_STR)
    assert reddit.user.me()  # We logged in?
    requestor = AuthenticatedRequestor(context=reddit)  # Our own adapter around PRAW
    for results in crawled(requestor.defaults(), requestor.about):
        add_if_absent(**results)


if __name__ == '__main__':
    main()