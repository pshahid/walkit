# Models

Lightweight documentation of what models should exist within application. This is just to document and flesh out application concerns.

* questions -- To gauge a user's interests you should ask them questions, each question is encapsulated with a model
  * id
  * text
* answer -- Counterpart to a question
  * id
  * text
* subreddit -- obvious
  * id
  * name
  * about
* subreddit_mentions -- less obvious, normalized form of what a subreddit mentions
  * subreddit_fkey
  * subreddit_fkey2

* user -- Later on down the line we may want to allow people to login; I would prefer to avoid this if possible, maybe by leveraging HTML5 local storage
  * name
  * probably some social login access tokens and crap
* users_interests -- mapping of username fkeys to 'interests', if interests are even normalized
  * user_fkey
  * interest_fkey

* interests -- table of 'interests' that users have answered from questions
