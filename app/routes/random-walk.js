import Ember from 'ember';

let subreddits = [
    {
        id: 1,
        name: 'personalfinance',
        url: 'https://reddit.com/r/personalfinance',
        description: 'A subreddit for learning about budgeting, debt, credit, and more.'
    },
    {
        id: 2,
        name: 'cats',
        url: 'https://reddit.com/r/cats',
        description: 'Cat.'
    },
    {
        id: 3,
        name: 'blep',
        url: 'https://reddit.com/r/blep',
        description: 'r/blep is a subreddit dedicated to animals blepping.'
    }
];

export default Ember.Route.extend({
    model() {
        const length = subreddits.length;
        const item = Math.floor(Math.random() * length);
        return subreddits[item];
    }
});
