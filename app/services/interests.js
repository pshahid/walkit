import Ember from 'ember';

export default Ember.Service.extend({
    // Sentiments; in conversation we would call this 'like' and 'dislike'
    // But there's also a third option: neutral; seen but no reaction, probably
    // the majority
    positive: new Map(),
    neutral: new Map(),
    negative: new Map(),
    init() {
        this._super(...arguments);
    },
    numPositive() {
        return this.get('positive').size;
    },
    numNegative() {
        return this.get('negative').size;
    },
    numNeutral() {
        return this.get('neutral').size;
    },
    like(subreddit) {
        var positive = this.get('positive');
        positive.set(subreddit.name, {
            subreddit: subreddit,
            action_date: new Date().toISOString()
        });
        this.deleteAction(subreddit, 'negative');
        this.deleteAction(subreddit, 'neutral');
        this.set('positive', positive);
    },
    neutral(subreddit) {
        var neutral = this.get('neutral');
        neutral.set(subreddit.name, {
            subreddit: subreddit,
            action_date: new Date().toISOString()
        });
        this.deleteAction(subreddit, 'negative');
        this.deleteAction(subreddit, 'positive');
    },
    deleteAction(subreddit, registryName) {
        var registry = this.get(registryName);
        if (registry.has(subreddit.name)) {
            registry.delete(subreddit.name)
        }
        this.set(registryName, registry);
    },
    dislike(subreddit) {
        var negative = this.get('negative');
        negative.set(subreddit.name, {
            subreddit: subreddit,
            action_date: new Date().toISOString()
        });
        this.deleteAction(subreddit, 'positive')
        this.deleteAction(subreddit, 'neutral');
        this.set('negative', negative);
    }
});
