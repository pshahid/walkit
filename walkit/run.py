import praw
from ingest.crawler import crawled

INI_NAME = 'walkit_backend'
USER_AGENT_STR = 'walkit - gathering a subreddit list'

def main():
    reddit = praw.Reddit(INI_NAME, user_agent=USER_AGENT_STR)
    assert reddit.user.me()
    for subreddit in crawled(reddit):
        print("Found: %s" % subreddit)


if __name__ == '__main__':
    main()