import Ember from 'ember';

export default Ember.Component.extend({
    random: Ember.inject.service(),
    history: Ember.inject.service(),
    subreddit: {id: 0, name: '', url: '', description: ''},
    actions: {
        getSubreddit() {
            const randomsvc = this.get('random');
            var self = this;
            randomsvc.meta();
            randomsvc.random(function(obj) {
                console.log("Random completed with obj");
                console.log(obj);
                self.set('subreddit', obj);
                var history = self.get('history');
                history.put(obj);
                console.log(history.all());
            })
            // this.set('subreddit', randomsvc.random());
        }
    }
});
