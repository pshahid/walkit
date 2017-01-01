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
    },
    {
        id: 4,
        name: 'indoor gardening',
        url: 'https://reddit.com/r/indoorgardening',
        description: 'A community for indoor gardeners'
    }
];

export default Ember.Service.extend({
    all() {
        console.log("Get all");
    },
    random() {
        const length = subreddits.length;
        const index = Math.floor(Math.random() * length);
        return subreddits[index];
    }
});
