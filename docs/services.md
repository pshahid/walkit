# Services

We need services to support the three flows of discovering subreddits: random, search, and discover. Whether to make a separate service per function is entirely up to how the single responsibility principle plays into this.

* Search service:
  * Purpose: find a subreddit if you already know part of its name or description
  * In-text search
  * Fuzzy match
  * Filters?
    * By classification?
    * By time created?
    * By popularity?

* Random walk service:
  * Purpose: Generate a random subreddit with or without limitations
  * Limit generation by discovered/undiscovered
  * Limit generation to NSFW vs SFW
  * Limit generation to private vs public
  * Client-side random selection of subreddits

* Discovery service:
  * Purpose: a refined random walk based on interests of users
  * Fetch questions and store answers
  * Fetch global interests list
  * Store selected interests
  * Get paginated list of subreddits

* Local storage service
  * Purpose: Service for storing data from current and previous sessions
  * Store overall count/progress of discovered vs undiscovered
  * Store names of discovered
  * Store past search queries
  * Store interests
  * Other analytics?
