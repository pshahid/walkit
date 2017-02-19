import Ember from 'ember';

export default Ember.Component.extend({
    history: Ember.inject.service(),
    interests: Ember.inject.service(),
    subreddit: {id: 0, name: '', url: '', description: ''},
    positive: Ember.computed('interests', function() {
        return this.get('interests').numPositive();
    }),
    negative: Ember.computed('interests', function() {
        return this.get('interests').numNegative();
    }),
    sentiment: 'neutral',
    init() {
        this._super(...arguments);
        this.next();
    },
    didInsertElement() {
        $(document).on('keyup', {_self: this}, this.keyUp.bind(this));
    },
    willDestroyElement() {
        $(document).off('keyup');
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
    keyUp(e) {
        const keycode = e.which || e.keycode;
        if (keycode === 39 || keycode === 68 ) {
            this.next();
        }

        if (keycode === 37 || keycode === 65) {
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
        },
        interested() {
            console.log("interested");
            console.log(arguments);
        }
    }
});
