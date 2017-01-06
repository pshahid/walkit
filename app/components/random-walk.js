import Ember from 'ember';

export default Ember.Component.extend({
    random: Ember.inject.service(),
    subreddit: {id: 0, name: '', url: '', description: ''},
    actions: {
        getSubreddit() {
            const randomsvc = this.get('random');
            this.set('subreddit', randomsvc.random());
        }
    }
});
