# Walkit

When I get bored I like to take random walks through Reddit. 

Unfortunately, it takes a long time to do that because Reddit's random button is quite slow. It would be nice at the start to at least have a faster 'random walk' mechanism than reddit, which is also not at the mercy of the reddit servers being up or down. The random button being in different places with each subreddit's theme is fairly annoying as well so this would remove that annoyance. Once these issues have been resolved we can move on to more interesting things, like tracking discovered subreddits, better ways for discovering new ones, and beyond.

# Goals

All goals are tied to a KPI (key performance indicator). Walkit attempts to meet the following goals:

* Allow random walks through subreddits, but have the time-to-click and MTTR be < 1 second.
  * KPI: MTTR from click to result is < 1 second
* Find subreddits that the user is interested in.
  * KPI: At least 1 subreddit is "found" interesting or novel to the user per session.
* Search for subreddits should work, and it should work for names and descriptions of subreddits.
  * KPI: Searching in-text should return results where the search string is matched against name and description of subreddits.

# Ideas for later

* Subreddit index: place to find subreddits rather than scrolling through a massive list like r/listofsubreddits
* As you go through subreddit discovery you can see the total amount discovered over existing.
* Do not show already-discovered subreddits


