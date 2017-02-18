import Ember from 'ember';


export default Ember.Service.extend({
    randomSubreddits: [],
    total: 0,
    seen: new Set(),
    init() {
        this._super(...arguments);
    },
    meta(cb) {
        var self = this;
        Ember.$.getJSON("http://localhost:8000/api/v1/subreddit?format=json").then(function(args) {
            self.set('total', args.meta.total_count);
            cb();
        });
    },
    all() {
        console.log("Get all");
    },
    _random(cb) {
        const length = this.get('total');
        var seen = this.get('seen');
        var index = 0;
        do {
            index = Math.floor(Math.random() * length);
        } while (seen.has(index));

        seen.add(index);
        this.set('seen', seen);

        Ember.$.getJSON(`http://localhost:8000/api/v1/subreddit/${index}/?format=json`).then(function(args) {
            cb(args);
        });
    },
    _ensure_total(cb) {
        const total = this.get('total');
        if (!total) {
            this.meta(this._random.bind(this, cb));
        } else {
            this._random(cb);
        }
    },
    _generate_random(total, cb) {

    },
    random(cb) {
        this._ensure_total(cb);
    }
});
