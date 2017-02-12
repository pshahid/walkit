import Ember from 'ember';


export default Ember.Service.extend({
    randomSubreddits: null,
    total: 0,
    init() {
        this._super(...arguments);
        this.set('randomSubreddits', []);
        this.meta();
    },
    meta() {
        var self = this;
        Ember.$.getJSON("http://localhost:8000/api/v1/subreddit?format=json").then(function(args) {
            self.set('total', args.meta.total_count);
        });
    },
    all() {
        console.log("Get all");
    },
    random(cb) {
        const total = this.get('total');
        if (!total) {
            console.log("No total!");
            console.log(total);
            this.meta();
        }
        const length = total;
        const index = Math.floor(Math.random() * length);
        Ember.$.getJSON(`http://localhost:8000/api/v1/subreddit/${index}/?format=json`).then(function(args) {
            console.log("RAndom!");
            console.log(args);
            cb(args);
            console.log("Called callback");
        });
    }
});
