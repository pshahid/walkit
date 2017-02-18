import Ember from 'ember';

export default Ember.Component.extend({
    history: Ember.inject.service(),
    subreddit: {id: 0, name: '', url: '', description: ''},
    init() {
        this._super(...arguments);
        this.next();
    },
    setSubreddit(subreddit) {
        this.set('subreddit', subreddit);
    },
    next() {
        const history = this.get('history');
        history.next(this.setSubreddit.bind(this));
    },
    previous() {
        const historysvc = this.get('history');
        const last = historysvc.back();
        this.set('subreddit', last);
    },
    keyUp: function(e) {
        if (e.which === 39) {
            this.next();
        }

        if (e.which === 37) {
            this.previous();
        }
    },
    actions: {
        handleNext() {
            this.next();
        },
        handlePrevious() {
            this.previous();
        },
        getSubreddit() {
            this.next();
        }
    }
});
